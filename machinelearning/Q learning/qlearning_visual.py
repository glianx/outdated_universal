import itertools
import time

import numpy as np
import cv2

from moviepy.editor import VideoClip


WORLD_HEIGHT = 16
WORLD_WIDTH = 9
WALL_FRAC = .2
NUM_WINS = 5
NUM_LOSE = 10


class GridWorld:

    def __init__(self, world_height=3, world_width=4, discount_factor=.5, default_reward=-.5, wall_penalty=-.6,
                 win_reward=5., lose_reward=-10., viz=True, patch_side=120, grid_thickness=2, arrow_thickness=3,
                 wall_locs=[[1, 1], [1, 2]], win_locs=[[0, 3]], lose_locs=[[1, 3]], start_loc=[0, 0],
                 reset_prob=.2):
        self.world = np.ones([world_height, world_width]) * default_reward
        self.reset_prob = reset_prob
        self.world_height = world_height
        self.world_width = world_width
        self.wall_penalty = wall_penalty
        self.win_reward = win_reward
        self.lose_reward = lose_reward
        self.default_reward = default_reward
        self.discount_factor = discount_factor
        self.patch_side = patch_side
        self.grid_thickness = grid_thickness
        self.arrow_thickness = arrow_thickness
        self.wall_locs = np.array(wall_locs)
        self.win_locs = np.array(win_locs)
        self.lose_locs = np.array(lose_locs)
        self.at_terminal_state = False
        self.auto_reset = True
        self.random_respawn = True
        self.step = 0
        self.viz_canvas = None
        self.viz = viz
        self.path_color = (128, 128, 128)
        self.wall_color = (0, 255, 0)
        self.win_color = (0, 0, 255)
        self.lose_color = (255, 0, 0)
        self.world[self.wall_locs[:, 0], self.wall_locs[:, 1]] = self.wall_penalty
        self.world[self.lose_locs[:, 0], self.lose_locs[:, 1]] = self.lose_reward
        self.world[self.win_locs[:, 0], self.win_locs[:, 1]] = self.win_reward
        spawn_condn = lambda loc: self.world[loc[0], loc[1]] == self.default_reward
        self.spawn_locs = np.array([loc for loc in itertools.product(np.arange(self.world_height),
                                                                     np.arange(self.world_width))
                                    if spawn_condn(loc)])
        self.start_state = np.array(start_loc)
        self.bot_rc = None
        self.reset()
        self.actions = [self.up, self.left, self.right, self.down, self.noop]
        self.action_labels = ['UP', 'LEFT', 'RIGHT', 'DOWN', 'NOOP']
        self.q_values = np.ones([self.world.shape[0], self.world.shape[1], len(self.actions)]) * 1. / len(self.actions)
        if self.viz:
            self.init_grid_canvas()
            self.video_out_fpath = 'shm_dqn_gridsolver-' + str(time.time()) + '.mp4'
            self.clip = VideoClip(self.make_frame, duration=15)

    def make_frame(self, t):
        self.action()
        frame = self.highlight_loc(self.viz_canvas, self.bot_rc[0], self.bot_rc[1])
        return frame

    def check_terminal_state(self):
        if self.world[self.bot_rc[0], self.bot_rc[1]] == self.lose_reward \
                or self.world[self.bot_rc[0], self.bot_rc[1]] == self.win_reward:
            self.at_terminal_state = True
            # print('------++++---- TERMINAL STATE ------++++----')
            # if self.world[self.bot_rc[0], self.bot_rc[1]] == self.win_reward:
            #     print('GAME WON! :D')
            # elif self.world[self.bot_rc[0], self.bot_rc[1]] == self.lose_reward:
            #     print('GAME LOST! :(')
            if self.auto_reset:
                self.reset()

    def reset(self):
        # print('Resetting')
        if not self.random_respawn:
            self.bot_rc = self.start_state.copy()
        else:
            self.bot_rc = self.spawn_locs[np.random.choice(np.arange(len(self.spawn_locs)))].copy()
        self.at_terminal_state = False

    def up(self):
        action_idx = 0
        # print(self.action_labels[action_idx])
        new_r = self.bot_rc[0] - 1
        if new_r < 0 or self.world[new_r, self.bot_rc[1]] == self.wall_penalty:
            return self.wall_penalty, action_idx
        self.bot_rc[0] = new_r
        reward = self.world[self.bot_rc[0], self.bot_rc[1]]
        self.check_terminal_state()
        return reward, action_idx

    def left(self):
        action_idx = 1
        # print(self.action_labels[action_idx])
        new_c = self.bot_rc[1] - 1
        if new_c < 0 or self.world[self.bot_rc[0], new_c] == self.wall_penalty:
            return self.wall_penalty, action_idx
        self.bot_rc[1] = new_c
        reward = self.world[self.bot_rc[0], self.bot_rc[1]]
        self.check_terminal_state()
        return reward, action_idx

    def right(self):
        action_idx = 2
        # print(self.action_labels[action_idx])
        new_c = self.bot_rc[1] + 1
        if new_c >= self.world.shape[1] or self.world[self.bot_rc[0], new_c] == self.wall_penalty:
            return self.wall_penalty, action_idx
        self.bot_rc[1] = new_c
        reward = self.world[self.bot_rc[0], self.bot_rc[1]]
        self.check_terminal_state()
        return reward, action_idx

    def down(self):
        action_idx = 3
        # print(self.action_labels[action_idx])
        new_r = self.bot_rc[0] + 1
        if new_r >= self.world.shape[0] or self.world[new_r, self.bot_rc[1]] == self.wall_penalty:
            return self.wall_penalty, action_idx
        self.bot_rc[0] = new_r
        reward = self.world[self.bot_rc[0], self.bot_rc[1]]
        self.check_terminal_state()
        return reward, action_idx

    def noop(self):
        action_idx = 4
        # print(self.action_labels[action_idx])
        reward = self.world[self.bot_rc[0], self.bot_rc[1]]
        self.check_terminal_state()
        return reward, action_idx

    def qvals2probs(self, q_vals, epsilon=1e-4):
        action_probs = q_vals - q_vals.min() + epsilon
        action_probs = action_probs / action_probs.sum()
        return action_probs

    def action(self):
        # print('================ ACTION =================')
        if self.at_terminal_state:
            print('At terminal state, please call reset()')
            exit()
        # print('Start position:', self.bot_rc)
        start_bot_rc = self.bot_rc[0], self.bot_rc[1]
        q_vals = self.q_values[self.bot_rc[0], self.bot_rc[1]]
        action_probs = self.qvals2probs(q_vals)
        reward, action_idx = np.random.choice(self.actions, p=action_probs)()
        # print('End position:', self.bot_rc)
        # print('Reward:', reward)
        alpha = np.exp(-self.step / 10e9)
        self.step += 1
        qv = (1 - alpha) * q_vals[action_idx] + alpha * (reward + self.discount_factor
                                                         * self.q_values[self.bot_rc[0], self.bot_rc[1]].max())
        self.q_values[start_bot_rc[0], start_bot_rc[1], action_idx] = qv
        if self.viz:
            self.update_viz(start_bot_rc[0], start_bot_rc[1])
        if np.random.rand() < self.reset_prob:
            # print('-----> Randomly resetting to a random spawn point with probability', self.reset_prob)
            self.reset()

    def highlight_loc(self, viz_in, i, j):
        starty = i * (self.patch_side + self.grid_thickness)
        endy = starty + self.patch_side
        startx = j * (self.patch_side + self.grid_thickness)
        endx = startx + self.patch_side
        viz = viz_in.copy()
        cv2.rectangle(viz, (startx, starty), (endx, endy), (255, 255, 255), thickness=self.grid_thickness)
        return viz

    def update_viz(self, i, j):
        starty = i * (self.patch_side + self.grid_thickness)
        endy = starty + self.patch_side
        startx = j * (self.patch_side + self.grid_thickness)
        endx = startx + self.patch_side
        patch = np.zeros([self.patch_side, self.patch_side, 3]).astype(np.uint8)
        if self.world[i, j] == self.default_reward:
            patch[:, :, :] = self.path_color
        elif self.world[i, j] == self.wall_penalty:
            patch[:, :, :] = self.wall_color
        elif self.world[i, j] == self.win_reward:
            patch[:, :, :] = self.win_color
        elif self.world[i, j] == self.lose_reward:
            patch[:, :, :] = self.lose_color
        if self.world[i, j] == self.default_reward:
            action_probs = self.qvals2probs(self.q_values[i, j])
            x_component = action_probs[2] - action_probs[1]
            y_component = action_probs[0] - action_probs[3]
            magnitude = 1. - action_probs[-1]
            s = self.patch_side // 2
            x_patch = int(s * x_component)
            y_patch = int(s * y_component)
            arrow_canvas = np.zeros_like(patch)
            vx = s + x_patch
            vy = s - y_patch
            cv2.arrowedLine(arrow_canvas, (s, s), (vx, vy), (255, 255, 255), thickness=self.arrow_thickness,
                            tipLength=0.5)
            gridbox = (magnitude * arrow_canvas + (1 - magnitude) * patch).astype(np.uint8)
            self.viz_canvas[starty:endy, startx:endx] = gridbox
        else:
            self.viz_canvas[starty:endy, startx:endx] = patch

    def init_grid_canvas(self):
        org_h, org_w = self.world_height, self.world_width
        viz_w = (self.patch_side * org_w) + (self.grid_thickness * (org_w - 1))
        viz_h = (self.patch_side * org_h) + (self.grid_thickness * (org_h - 1))
        self.viz_canvas = np.zeros([viz_h, viz_w, 3]).astype(np.uint8)
        for i in range(org_h):
            for j in range(org_w):
                self.update_viz(i, j)

    def solve(self):
        if not self.viz:
            while True:
                self.action()
        else:
            self.clip.write_videofile(self.video_out_fpath, fps=460)


def gen_world_config(h, w, wall_frac=.5, num_wins=2, num_lose=3):
    n = h * w
    num_wall_blocks = int(wall_frac * n)
    wall_locs = (np.random.rand(num_wall_blocks, 2) * [h, w]).astype(np.int)
    win_locs = (np.random.rand(num_wins, 2) * [h, w]).astype(np.int)
    lose_locs = (np.random.rand(num_lose, 2) * [h, w]).astype(np.int)
    return wall_locs, win_locs, lose_locs


if __name__ == '__main__':
    wall_locs, win_locs, lose_locs = gen_world_config(WORLD_HEIGHT, WORLD_WIDTH, WALL_FRAC, NUM_WINS, NUM_LOSE)
    g = GridWorld(world_height=WORLD_HEIGHT, world_width=WORLD_WIDTH,
                  wall_locs=wall_locs, win_locs=win_locs, lose_locs=lose_locs, viz=True)
    g.solve()
    k = 0
import gamelib
import random
import math
import warnings
from sys import maxsize
import json

"""
Most of the algo code you write will be in this file unless you create new
modules yourself. Start by modifying the 'on_turn' function.

Advanced strategy tips: 

  - You can analyze action frames by modifying on_action_frame function

  - The GameState.map object can be manually manipulated to create hypothetical 
  board states. Though, we recommended making a copy of the map to preserve 
  the actual current map state.
"""

"""
To-do:
fix attack support cost: # supports, turret + wall position, upgrade
algorithm attack pattern
demolisher line strategy    
respawn and upgrade only valuable defenses
if enemy wall in front of corner wall, remove and do not upgrade
vertical line attack?

Current notes
why spawn 5, not 3?
"""

class AlgoStrategy(gamelib.AlgoCore):
    def __init__(self):
        super().__init__()
        seed = random.randrange(maxsize)
        random.seed(seed)
        gamelib.debug_write('Random seed: {}'.format(seed))


    def on_game_start(self, config):
        """ 
        Read in config and perform any initial setup here 
        """
        self.config = config
        global WALL, SUPPORT, TURRET, SCOUT, DEMOLISHER, INTERCEPTOR, MP, SP
        WALL = config["unitInformation"][0]["shorthand"]
        SUPPORT = config["unitInformation"][1]["shorthand"]
        TURRET = config["unitInformation"][2]["shorthand"]
        SCOUT = config["unitInformation"][3]["shorthand"]
        DEMOLISHER = config["unitInformation"][4]["shorthand"]
        INTERCEPTOR = config["unitInformation"][5]["shorthand"]
        MP = 1
        SP = 0

        # This is a good place to do initial setup
        self.scored_on_locations = []

        # spawned structure locations
        self.spawned_structure_locations = []

        # upgraded structure locations
        self.upgraded_structure_locations = []

        # damaged structure locations
        self.damaged_structure_locations = []

        # killed structure locations
        self.killed_structure_locations = []

        # hard coded structure locations
        self.turret_locations = [[1, 12], [26, 12], [7, 9], [12, 9], [16, 9], [20, 9]]
        self.wall_locations = [[0, 13], [1, 13], [2, 13], [25, 13], [26, 13], [27, 13], [6, 10], [7, 10], [8, 10], [9, 10], [10, 10], [11, 10], [16, 10], [17, 10], [18, 10], [19, 10], [20, 10], [21, 10]]
        self.self_destruct_wall_locations = [[12,10],[13,10],[14,9],[15,10]]
        self.diagonal_funnel_wall_locations = [[3,12],[4,11],[5,10],[24,12],[23,11],[22,10]]
        self.extra_wall_locations = []

        # self.turret_locations = [[11,13]]
        # self.wall_locations = [[14,13]]
        # self.self_destruct_wall_locations = []
        # self.diagonal_funnel_wall_locations = []

    def on_turn(self, turn_state):
        """
        This function is called every turn with the game state wrapper as
        an argument. The wrapper stores the state of the arena and has methods
        for querying its state, allocating your current resources as planned
        unit deployments, and transmitting your intended deployments to the
        game engine.
        """
        game_state = gamelib.GameState(self.config, turn_state)
        gamelib.debug_write('Performing turn {} of your custom algo strategy'.format(game_state.turn_number))
        game_state.suppress_warnings(True)  #Comment or remove this line to enable warnings.

        # update dynamic structure location arrays
        self.all_wall_locations = self.wall_locations + self.self_destruct_wall_locations + self.diagonal_funnel_wall_locations + self.extra_wall_locations
        self.all_structure_locations = self.turret_locations + self.all_wall_locations

        self.starter_strategy(game_state)

        game_state.submit_turn()

    """
    NOTE: All the methods after this point are part of the sample starter-algo
    strategy and can safely be replaced for your custom algo.
    """

    def starter_strategy(self, game_state):
        # # if enemy MP < 6 (assume just attacked - enemy usually won't attack twice)
        # # and my MP >= 9 (achieved after 2 moves - every 3 turns min) then attack
        # if game_state.get_resource(MP, 1) < 6 and game_state.get_resource(MP, 0) >= 9:

        gamelib.debug_write("PREV_SPAWNED @: {}".format(self.spawned_structure_locations))
        gamelib.debug_write("PREV_KILLED @: {}".format(self.killed_structure_locations))

        # build initial defense
        if game_state.turn_number == 0:
            self.build_general_defense(game_state)

        # spawn first round defense
        if game_state.turn_number % 3 == 0:
            self.defense_configuration(game_state)

        # analyze first round losses and upgrade second round defense
        if game_state.turn_number % 3 == 1:
            self.analyze_previous_losses(game_state)
            self.defense_configuration(game_state)

        # analyze second round losses and attack
        if game_state.turn_number % 3 == 2:
            # self.analyze_previous_losses(game_state)
            self.attack_configuration(game_state)

        gamelib.debug_write("JUST_SPAWNED @: {}".format(self.spawned_structure_locations))
        gamelib.debug_write("JUST_KILLED @: {}".format(self.killed_structure_locations))

    def attack_configuration(self,game_state):
        # We can spawn moving units on our edges so a list of all our edge locations
        friendly_left_edge = game_state.game_map.get_edge_locations(game_state.game_map.BOTTOM_LEFT)
        friendly_right_edge = game_state.game_map.get_edge_locations(game_state.game_map.BOTTOM_RIGHT)
        friendly_edges = friendly_left_edge + friendly_right_edge

        # Find enemy edges
        enemy_left_edge = game_state.game_map.get_edge_locations(game_state.game_map.TOP_LEFT)
        enemy_right_edge = game_state.game_map.get_edge_locations(game_state.game_map.TOP_RIGHT)
        enemy_edges = enemy_left_edge + enemy_right_edge      
        
        # Remove locations that are blocked by our own structures 
        # since we can't deploy units there.
        deploy_locations = self.filter_blocked_locations(game_state, friendly_edges)

        # find least damage spawn location
        best_location = self.least_damage_spawn_location(game_state, deploy_locations)
        bx, by = best_location[0], best_location[1]

        # find path to edge
        best_path = game_state.find_path_to_edge(best_location)


        # check if path is a self-destruct path
        if best_path[-1] not in enemy_edges:
            # path is a self-destruct path

            # if best location is a corner, remove corners from deploy_locations and find next best location
            if best_location in [[13,0],[14,0]]:
                deploy_locations.remove([13,0])
                deploy_locations.remove([14,0])

                best_location = self.least_damage_spawn_location(game_state, deploy_locations)
                bx, by = best_location[0], best_location[1]
                best_path = game_state.find_path_to_edge(best_location)

            # create support locations surrounding unit path
            support_locations = []

            # find follow location and follow path
            if best_location in friendly_left_edge:
                follow_location = [bx + 1, by - 1]
                follow_path = [[bx + 1, by], [bx + 1, by - 1]]

                # add redirection support
                support_locations.append([bx + 1, by + 1])
                game_state.attempt_spawn(SUPPORT, support_locations)

            elif best_location in friendly_right_edge:
                follow_location = [bx - 1, by - 1]
                follow_path = [[bx - 1, by],[bx - 1, by - 1]]

                # add redirection support
                support_locations.append([bx - 1, by + 1])
                game_state.attempt_spawn(SUPPORT, support_locations)

            # update best_path to consider redirection support
            best_path = game_state.find_path_to_edge(best_location)

            # generate surrounding support locations
            for path_location in best_path:
                for surrounding_location in game_state.game_map.get_locations_in_range(path_location, gamelib.GameUnit(SUPPORT, game_state.config).shieldRange):
                    if surrounding_location not in best_path + follow_path:
                        support_locations.append(surrounding_location)
            
            # spawn supports
            game_state.attempt_spawn(SUPPORT, support_locations)

            # spawn self-destruct and follower scouts
            game_state.attempt_spawn(SCOUT, best_location, math.floor(game_state.get_resource(MP) * .4))
            game_state.attempt_spawn(SCOUT, follow_location, 1000)

            # refund all supports for next defensive turn
            game_state.attempt_remove(support_locations)

        else:
            # path reaches enemy edge

            # create support locations surrounding unit path
            support_locations = []

            # generate surrounding support locations
            for path_location in best_path:
                for surrounding_location in game_state.game_map.get_locations_in_range(path_location, gamelib.GameUnit(SUPPORT, game_state.config).shieldRange):
                    if surrounding_location not in best_path:
                        support_locations.append(surrounding_location)

            # spawn supports
            game_state.attempt_spawn(SUPPORT, support_locations)

            # spawn scouts
            game_state.attempt_spawn(SCOUT, best_location, 1000)

            # refund all supports for next defensive turn
            game_state.attempt_remove(support_locations)

    def defense_configuration(self,game_state):
        # build general defense
        self.build_general_defense(game_state)

        # respawn 5 most recently killed structures with upgrade
        for structure_location in list(reversed(self.killed_structure_locations))[:5]:
            if structure_location in self.turret_locations:
                game_state.attempt_spawn(TURRET, structure_location)
            elif structure_location in self.all_wall_locations:
                game_state.attempt_spawn(WALL, structure_location)
            game_state.attempt_upgrade(structure_location)

        # build extra structures around 5 most recently killed structures
        for structure_location in list(reversed(self.killed_structure_locations))[:5]:
            x,y = structure_location

            if structure_location in self.turret_locations:
                neighbor_locations = [[x - 1, y], [x + 1, y], [x, y - 1], [x - 1, y - 1], [x + 1, y - 1]]
                for _ in range(0,self.killed_structure_locations.count(structure_location) - 2, 1):
                    for j in range(0, len(neighbor_locations), 1):
                        if game_state.attempt_spawn(TURRET, neighbor_locations[j]):
                            self.turret_locations.append(neighbor_locations[j])
                            break

                # # spawn turret left / right: avoid self_destruct location
                # if [x - 1, y] not in [[13,9],[13,8],[14,8],[15,8],[15,9]]:
                #     game_state.attempt_spawn(TURRET, [x - 1, y])
                # else:
                #     game_state.attempt_spawn(TURRET, [x + 1, y])

            elif structure_location in self.all_wall_locations:
                neighbor_locations = [[x, y - 1], [x - 1, y - 1], [x + 1, y - 1]]
                for _ in range(0,self.killed_structure_locations.count(structure_location) - 2, 1):
                    for j in range(0, len(neighbor_locations), 1):
                        if game_state.attempt_spawn(WALL, neighbor_locations[j]):
                            self.extra_wall_locations.append(neighbor_locations[j])
                            break

                # # upgrade turret behind or spawn wall behind
                # if not game_state.attempt_upgrade([x, y - 1]):
                #     game_state.attempt_spawn(WALL, [x, y - 1])

        # # upgrade general structures with remaining structure points
        # self.general_upgrades(game_state)

        # # if will attack next turn, then refund all structures for next attacking turn
        # if game_state.get_resource(MP, 1) < 6 and game_state.project_future_MP() >= 9:
        if game_state.turn_number % 3 == 1:
            # update dynamic structure location arrays
            self.all_wall_locations = self.wall_locations + self.self_destruct_wall_locations + self.diagonal_funnel_wall_locations + self.extra_wall_locations
            self.all_structure_locations = self.turret_locations + self.all_wall_locations
            game_state.attempt_remove(self.all_structure_locations)
    
    def build_general_defense(self, game_state):
        # corner and line turrets
        for turret_location in self.turret_locations:
            if game_state.attempt_spawn(TURRET, turret_location) and turret_location not in self.spawned_structure_locations:
                self.spawned_structure_locations.append(turret_location)

        for wall_location in self.all_wall_locations:
            if game_state.attempt_spawn(WALL, wall_location) and wall_location not in self.spawned_structure_locations:
                self.spawned_structure_locations.append(wall_location)

    def analyze_previous_losses(self, game_state):
        # check if structure has been killed or damaged
        for structure_location in self.spawned_structure_locations:
            # x, y = structure_location
            # unit = game_state.game_map[x][y]
            unit = game_state.contains_stationary_unit(structure_location)
            if (not unit): # or (gamelib.GameUnit(unit, game_state.config).health < gamelib.GameUnit(unit, game_state.config).max_health):
                self.killed_structure_locations.append(structure_location)

    def general_upgrades(self, game_state):
        # upgrade corner walls
        upgrade_wall_locations = [[1,13],[2,13],[26,13],[25,13],[0,13],[27,13]]
        game_state.attempt_upgrade(upgrade_wall_locations)

        # upgrade self-destruct walls
        upgrade_wall_locations = [[13,10],[15,10],[14,9]]
        game_state.attempt_upgrade(upgrade_wall_locations)

        # upgrade walls in front of turrets
        upgrade_wall_locations = [[x, y+1] for [x,y] in self.turret_locations]
        game_state.attempt_upgrade(upgrade_wall_locations)

        # upgrade turrets
        game_state.attempt_upgrade(self.turret_locations)

        # upgrade all walls
        game_state.attempt_upgrade(self.all_wall_locations)

    def least_damage_spawn_location(self, game_state, location_options):
        """
        This function will help us guess which location is the safest to spawn moving units from.
        It gets the path the unit will take then checks locations on that path to 
        estimate the path's damage risk.
        """
        damages = []
        # Get the damage estimate each path will take
        for location in location_options:
            path = game_state.find_path_to_edge(location)
            damage = 0
            for path_location in path:
                # Get number of enemy turrets that can attack each location and multiply by turret damage
                damage += len(game_state.get_attackers(path_location, 0)) * gamelib.GameUnit(TURRET, game_state.config).damage_i
            damages.append(damage)
        
        # Now just return the location that takes the least damage
        return location_options[damages.index(min(damages))]

    def filter_blocked_locations(self, game_state, locations):
        filtered = []
        for location in locations:
            if not game_state.contains_stationary_unit(location):
                filtered.append(location)
        return filtered

    def on_action_frame(self, turn_string):
        """
        This is the action frame of the game. This function could be called 
        hundreds of times per turn and could slow the algo down so avoid putting slow code here.
        Processing the action frames is complicated so we only suggest it if you have time and experience.
        Full doc on format of a game frame at in json-docs.html in the root of the Starterkit.
        """
        # Let's record at what position we get scored on
        state = json.loads(turn_string)
        events = state["events"]
        breaches = events["breach"]
        for breach in breaches:
            location = breach[0]
            unit_owner_self = True if breach[4] == 1 else False
            # When parsing the frame data directly, 
            # 1 is integer for yourself, 2 is opponent (StarterKit code uses 0, 1 as player_index instead)
            if not unit_owner_self:
                # gamelib.debug_write("Got scored on at: {}".format(location))
                self.scored_on_locations.append(location)
                # gamelib.debug_write("All locations: {}".format(self.scored_on_locations))

if __name__ == "__main__":
    algo = AlgoStrategy()
    algo.start()

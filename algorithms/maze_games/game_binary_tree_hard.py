# generate maze

import random
import os
import time

n = 21
r = 3

# grid[y][x] = [on/off, type]
grid = [[[0,1] for x in range(n)] for y in range(n)]

start_y,start_x = 0,0
end_y,end_x = n-1,n-1

grid[start_y][start_x][1] = 4
grid[end_y][end_x][1] = 5

def display():
    os.system('clear')
    for row in grid:
        for node in row:
            print([['  ' for _ in range(6)],['  ','⬜','🟥','🟩','🟩','🟩']][node[0]][node[1]], end = '')
        print()

def around_nodes(y,x):
    arounds = [[y,x-2],[y-2,x]]
    return [[a,b] for [a,b] in arounds if 0 <= a <= n-1 and 0 <= b <= n-1]

def visit_wall_between(y1,x1,y2,x2):
    grid[int((y1+y2)/2)][int((x1+x2)/2)][1] = 0

def binary_tree():
    for y in range(0,n,2):
        for x in range(0,n,2):
            if (y,x) != (start_y,start_x):
                y2,x2 = random.choice(around_nodes(y,x))

                if grid[y][x][1] == 1:
                    grid[y][x][1] = 0
                if grid[y2][x2][1] == 1:
                    grid[y2][x2][1] = 0
                    
                visit_wall_between(y2,x2,y,x)

        


binary_tree()
display()


# ====================================================================================================

# gameplay

import sys,tty,termios
class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def around(y,x,r):
    around_pos = [(y+a,x+b) for a in range(-r,r+1,1) for b in range(-r,r+1,1)]
    return [[a,b] for [a,b] in around_pos if 0 <= a <= n-1 and 0 <= b <= n-1]

y,x = 0,0
prev_type = grid[y][x][1]
explored_nodes = []
expanded_nodes = set()


start = time.time()

while True:

    if [y,x] == [n-1,n-1]:
        break

    input_ = _Getch()()

    grid[y][x][1] = 0
    for [a,b] in around(y,x,r):
        grid[a][b][0] = 0

    # change y,x with arrow keys
    if input_ == '\x1b[A':
        if y != 0 and grid[y-1][x][1] != 1:
            y -= 1
    elif input_ == '\x1b[B':
        if y != n-1 and grid[y+1][x][1] != 1:
            y += 1
    elif input_ == '\x1b[C':
        if x != n-1 and grid[y][x+1][1] != 1:
            x += 1
    elif input_ == '\x1b[D':
        if x != 0 and grid[y][x-1][1] != 1: 
            x -= 1

    # set surrounding nodes to visible

    for [a,b] in around(y,x,r):
        grid[a][b][0] = 1
        expanded_nodes.add((a,b))

    # make current node visible and colour green

    grid[y][x][0] = 1
    grid[y][x][1] = 3
    explored_nodes.append((y,x))
    expanded_nodes.remove((y,x))

    display()

# set all visible
for row in grid:
    for node in row:
        node[0] = 1

# show explored, expanded nodes
for [y,x] in explored_nodes:
    grid[y][x][1] = 2
for [y,x] in expanded_nodes:
    if grid[y][x][1] == 0:
        grid[y][x][1] = 3

display()
print('runtime:', time.time() - start)
print('explored:',len(set(explored_nodes)))
print('steps:', len(explored_nodes))
print('expanded:',len(expanded_nodes))

input()
# ====================================================================================================

# # A star Algorithm

# inf = float('inf')

# for y,row in enumerate(grid):
#     for x in range(len(row)):
#         grid[y][x].pop(0)
#         for item in [inf,inf,inf,y,x,None,None]:
#             grid[y][x].append(item)

# grid[0][0][0] = 4
# grid[0][0][2] = 0

# end_y,end_x = n-1,n-1
# grid[end_y][end_x][0] = 4

# print(grid[0])
# input()

# def display():
#     # os.system('clear')
#     for row in grid:
#         for node in row:
#             # ⬜⬛🟥🟩🟦 01234 abcde _#*^+ '_x*#X
#             print(['⬜','  ','🟥','🟩','🟦','🟦'][node[0]], end='')

#         print()


# def d(a,b):
#     dy = abs(a[0]-b[0])
#     dx = abs(a[1]-b[1])
#     return 14 * min(dx,dy) + 10 * abs(dx-dy)

# def around(y,x):
#     around_pos = [[y-1,x-1],[y-1,x],[y-1,x+1],[y,x-1],[y,x+1],[y+1,x-1],[y+1,x],[y+1,x+1]]
#     return [[a,b] for [a,b] in around_pos if 0 <= a <= n-1 and 0 <= b <= n-1 and grid[a][b][0] != 1]

# expanded_cells = []
# explored_cells = []

# def explore(y,x):
#     if [x,y] != [0,0]: 
#         explore_node = grid[y][x]
#         explore_node[0] = 2
#         explored_cells.append(explore_node)
#         if explore_node in expanded_cells:
#             expanded_cells.remove(explore_node)
#     for [a,b] in around(y,x):
#         node = grid[a][b]
#         if node[0] in (0,2,3): 
#             node[0] = 3
#             expanded_cells.append(node)

#         if grid[y][x][2] + d([y,x],[a,b]) < node[2]:
#             node[2] = grid[y][x][2] + d([y,x],[a,b])
#         if d([end_y,end_x],[a,b]) < node[3]:
#             node[3] = d([end_y,end_x],[a,b])
#         if node[2] + node[3] < node[1]:
#             node[1] = node[2] + node[3]
#             node[6],node[7] = y,x


# y,x = 0,0

# os.system('clear')
# display()
# input()

# start = time.time()

# while grid[end_y][end_x][1] == inf:
#     os.system('clear')

#     explore(y,x)
    
#     min_fcost = inf
#     min_hcost = inf

#     for node in expanded_cells:
#         if node[1] < min_fcost:
#             min_fcost = node[1]
#             min_hcost = node[3]
#             y,x = node[4],node[5]

#         elif node[1] == min_fcost:
#             if node[3] < min_hcost:
#                 min_hcost = node[3] 
#                 y,x = node[4],node[5]
    
#     display()
#     # input()
#     # time.sleep(0.01)

#     if len(expanded_cells) == 0:
#         print('no possible path')
#         exit()

# runtime = time.time() - start

# y,x = end_y,end_x

# os.system('clear')
# display()
# input()

# while [y,x] != [0,0]:
#     os.system('clear')
#     grid[y][x][0] = 4
#     y,x = grid[y][x][6],grid[y][x][7]
#     display()
#     time.sleep(0.01)

# os.system('clear')
# display()

# print('runtime:',runtime)
# print('explored:',len(explored_cells))
# print('expanded:',len(expanded_cells))
# print('fcost:',grid[end_y][end_x][1])
# print('minimum fcost:',d([0,0],[end_y,end_x]))



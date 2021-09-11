import os
os.system('clear')
import time
import random

n = 19

inf = float('inf')
grid = [[[random.choice([0,0,1]),inf,inf,inf,y,x,None,None] for x in range(n)] for y in range(n)]
    
grid[0][0][0] = 4
grid[1][1][0] = 0

grid[n-2][n-2][0] = 0
grid[0][0][2] = 0

end_y,end_x = n-1,n-1
grid[end_y][end_x][0] = 4

def display():
    for row in grid:
        for node in row:
            # ⬜⬛🟥🟩🟦 01234 abcde _#*^+ '_x*#X
            print('⬜⬛🟥🟩🟦'[node[0]], end='')

        print()


def d(a,b):
    dy = abs(a[0]-b[0])
    dx = abs(a[1]-b[1])
    return 14 * min(dx,dy) + 10 * abs(dx-dy)

def around(y,x):
    around_pos = [[y-1,x-1],[y-1,x],[y-1,x+1],[y,x-1],[y,x+1],[y+1,x-1],[y+1,x],[y+1,x+1]]
    return [[a,b] for [a,b] in around_pos if 0 <= a <= n-1 and 0 <= b <= n-1 and grid[a][b][0] != 1]

def floors():
    grid = [[[0,inf,inf,inf,y,x,None,None] for x in range(n)] for y in range(n)]

    for i in range(len(grid[0])):
        for j in range(5):
            if i != 5:
                grid[4*j+2][i][0] = 1

expanded_cells = []
explored_cells = []

def explore(y,x):
    if [x,y] != [0,0]: 
        explore_node = grid[y][x]
        explore_node[0] = 2
        explored_cells.append(explore_node)
        if explore_node in expanded_cells:
            expanded_cells.remove(explore_node)
    for [a,b] in around(y,x):
        node = grid[a][b]
        if node[0] == 0: 
            node[0] = 3
            expanded_cells.append(node)

        if grid[y][x][2] + d([y,x],[a,b]) < node[2]:
            node[2] = grid[y][x][2] + d([y,x],[a,b])
        if d([end_y,end_x],[a,b]) < node[3]:
            node[3] = d([end_y,end_x],[a,b])
        if node[2] + node[3] < node[1]:
            node[1] = node[2] + node[3]
            node[6],node[7] = y,x


y,x = 0,0

display()
input()

start = time.time()

while grid[end_y][end_x][1] == inf:
    os.system('clear')

    explore(y,x)
    
    min_fcost = inf
    min_hcost = inf

    for node in expanded_cells:
        if node[1] < min_fcost:
            min_fcost = node[1]
            min_hcost = node[3]
            y,x = node[4],node[5]

        elif node[1] == min_fcost:
            if node[3] < min_hcost:
                min_hcost = node[3] 
                y,x = node[4],node[5]
    
    display()
    # input()
    # time.sleep(0.01)

    if len(expanded_cells) == 0:
        print('no possible path')
        exit()

runtime = time.time() - start

y,x = end_y,end_x

while [y,x] != [0,0]:
    os.system('clear')
    grid[y][x][0] = 4
    y,x = grid[y][x][6],grid[y][x][7]
    display()
    time.sleep(0.01)

print('runtime:',runtime)
print('explored:',len(explored_cells))
print('expanded:',len(expanded_cells))
print('fcost:',grid[end_y][end_x][1])
print('minimum fcost:',d([0,0],[end_y,end_x]))


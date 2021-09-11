import random
import os
import time

n = 21
grid = [[1 for x in range(n)] for y in range(n)]

start_y,start_x = 0,0
end_y,end_x = n-1,n-1

grid[start_y][start_x] = 4
grid[end_y][end_x] = 5

def display():
    os.system('clear')
    for row in grid:
        for node in row: 
            print(['⬜','  ','🟥','🟩','🟦','🟦'][node], end = '')
        print()

def around_nodes(y,x):
    arounds = [[y,x+2],[y+2,x]]
    return [[a,b] for [a,b] in arounds if 0 <= a <= n-1 and 0 <= b <= n-1]

def visit_wall_between(y1,x1,y2,x2):
    grid[int((y1+y2)/2)][int((x1+x2)/2)] = 0

def binary_tree():
    for y,row in enumerate(grid):
        for x,node in enumerate(row):
            if x % 2 == 0 and y % 2 == 0:
                if (y,x) != (end_y,end_x):
                    y2,x2 = random.choice(around_nodes(y,x))

                    if grid[y][x] == 1:
                        grid[y][x] = 0
                    if grid[y2][x2] == 1:
                        grid[y2][x2] = 0
                        
                    visit_wall_between(y2,x2,y,x)
                    display()
                    # time.sleep(0.1)
        
display()
input()

start = time.time()  

binary_tree()

print(time.time() - start)


# ============================================================================================================


inf = float('inf')

for y,row in enumerate(grid):
    for x in range(len(row)):
        grid[y][x] = [grid[y][x]]
        for item in [inf,inf,inf,y,x,None,None]:
            grid[y][x].append(item)

grid[0][0][0] = 4
grid[0][0][2] = 0

end_y,end_x = n-1,n-1
grid[end_y][end_x][0] = 4

def display():
    # os.system('clear')
    for row in grid:
        for node in row:
            # ⬜⬛🟥🟩🟦 01234 abcde _#*^+ '_x*#X
            print(['⬜','  ','🟥','🟩','🟦','🟦'][node[0]], end='')

        print()


def d(a,b):
    dy = abs(a[0]-b[0])
    dx = abs(a[1]-b[1])
    return 14 * min(dx,dy) + 10 * abs(dx-dy)

def around(y,x):
    around_pos = [[y-1,x-1],[y-1,x],[y-1,x+1],[y,x-1],[y,x+1],[y+1,x-1],[y+1,x],[y+1,x+1]]
    return [[a,b] for [a,b] in around_pos if 0 <= a <= n-1 and 0 <= b <= n-1 and grid[a][b][0] != 1]

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

os.system('clear')
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

os.system('clear')
display()
input()

while [y,x] != [0,0]:
    os.system('clear')
    grid[y][x][0] = 4
    y,x = grid[y][x][6],grid[y][x][7]
    display()
    time.sleep(0.01)

os.system('clear')
display()

print('runtime:',runtime)
print('explored:',len(explored_cells))
print('expanded:',len(expanded_cells))
print('fcost:',grid[end_y][end_x][1])
print('minimum fcost:',d([0,0],[end_y,end_x]))


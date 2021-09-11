# generate maze

import random
import os
import time

n = 21

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
            print([['  ' for _ in range(6)],['  ','⬜','🟥','🟩','🟦','🟦']][node[0]][node[1]], end = '')
        print()

def around_nodes(y,x):
    arounds = [[y,x+2],[y+2,x]]
    return [[a,b] for [a,b] in arounds if 0 <= a <= n-1 and 0 <= b <= n-1]

def visit_wall_between(y1,x1,y2,x2):
    grid[int((y1+y2)/2)][int((x1+x2)/2)][1] = 0

def binary_tree():
    for y in range(0,n,2):
        for x in range(0,n,2):
            if (y,x) != (end_y,end_x):
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
expanded_nodes = []

r = 3
while True:

    if [y,x] == [n-1,n-1]:
        break

    input_ = _Getch()()

    grid[y][x][1] = 0
    for [a,b] in around(y,x,r):
        grid[a][b][0] = 0

    # change y,x with arrow keys
    if input_ == '\x1b[A':
        if y != 0:
            if grid[y-1][x][1] != 1:
                y -= 1
    elif input_ == '\x1b[B':
        if y != n-1:
            if grid[y+1][x][1] != 1:
                y += 1
    elif input_ == '\x1b[C':
        if x != n-1:
            if grid[y][x+1][1] != 1:
                x += 1
    elif input_ == '\x1b[D':
        if x != 0:
            if grid[y][x-1][1] != 1: 
                x -= 1

    # set surrounding nodes to visible

    for [a,b] in around(y,x,r):
        grid[a][b][0] = 1
        expanded_nodes.append([a,b])

    # make current node visible and colour green

    grid[y][x][0] = 1
    grid[y][x][1] = 3
    explored_nodes.append([y,x])
    expanded_nodes.remove([y,x])

    
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
print('Congratulations!')
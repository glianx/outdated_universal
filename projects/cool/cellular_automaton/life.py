import random
import os
os.system('clear')
import time
# 🟥🟧🟨🟩🟦🟪⬛️⬜️🟫
n = 30
alives = ['⬜️','🦊','🔥','🌎','🔥', '🌿', '🔥','🔥','❌','🐟','🦠','😂',]
deads  = ['🟦','🐰','💣','🌑','💦', '💩', '🌲','🌎','⭕️','💦','😂','💀',]
i = 1
alive = alives[i]
dead = deads[i]
border = deads[i]
grid = [[0 for x in range(n)] for y in range(n)]
grid2 = [[dead for x in range(n)] for y in range(n)]
grid2[0] = grid2[n-1] = [border for x in range(n)]

for y in range(n):
    grid2[y][0] = border
    grid2[y][n-1] = border

def display():
    os.system('clear')
    for row in grid2:
        for square in row:
            print(square, end = '')
        print()

def randomgrid():
    for y in range(n):
        for x in range(n):
            if x not in (0,n-1) and y not in (0,n-1):
                if random.choice([0,1,2]) == 0:
                    grid[y][x] = 1
                    grid2[y][x] = alive

def return_neighbours(x,y):
    neighbour8 = (grid[y][x+1],grid[y][x-1],grid[y+1][x],grid[y-1][x],\
                grid[y+1][x+1],grid[y+1][x-1],grid[y-1][x+1],grid[y-1][x-1])
    return neighbour8

def next_gen():
    born = []
    killed = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            surrounding_live = 0
            if y == 0 or y == len(grid) - 1: continue
            if x == 0 or x == len(grid[y]) - 1: continue

            for neighbour in return_neighbours(x,y):
                surrounding_live += neighbour

            if grid[y][x] == 1:
                if surrounding_live not in (2,3):
                    killed.append([y,x])
            if grid[y][x] == 0:
                if surrounding_live == 3:
                    born.append([y,x])
    for [y,x] in born:
        grid[y][x] = 1
        grid2[y][x] = alive
    for [y,x] in killed:
        grid[y][x] = 0
        grid2[y][x] = dead


randomgrid()
display()
time.sleep(3)

while True:
    display()
    time.sleep(0.1)
    next_gen()
        

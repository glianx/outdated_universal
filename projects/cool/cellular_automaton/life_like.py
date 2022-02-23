import random
import os
os.system('clear')
import time
# 🟥🟧🟨🟩🟦🟪⬛️⬜️🟫
print('enter #s of live neighbours for birth and survival')
inputB = input('enter B: ')
inputS = input('enter S: ')

alive_frequency = 3 # int(input('enter alive frequency: 1/'))
generation_speed = 1 # int(input('enter generation speed: 0.'))

B = [int(x) for x in inputB]
S = [int(x) for x in inputS]

n = 30

alive = '🟦'
dead = '⬜️'

grid = [[0 for x in range(n)] for y in range(n)]
grid2 = [[dead for x in range(n)] for y in range(n)]

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
                if random.randrange(alive_frequency) == 0:
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
                if surrounding_live not in S:
                    killed.append([y,x])
            if grid[y][x] == 0:
                if surrounding_live in B:
                    born.append([y,x])

    for [y,x] in born:
        grid[y][x] = 1
        grid2[y][x] = alive
    for [y,x] in killed:
        grid[y][x] = 0
        grid2[y][x] = dead


randomgrid()
display()
while True:
    # if not input():
    display()
    time.sleep(generation_speed/10)
    next_gen()
        

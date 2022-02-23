import random
import time
import os
os.system('clear')

def display():
    for row in grid:
        for node in row:
            print(['  ','🟩','🟥'][node], end = '')
        print()

n = 10
grid = [[0 for x in range(n)] for y in range(n)]

N,E,S,W = [-1,0],[0,1],[1,0],[0,-1]

start_y,start_x = 5,2
k = 5

snake = [[start_y,start_x+i] for i in range(k)]

# snake head pos
y,x = start_y,start_x+k-1

for [a,b] in snake:
    grid[a][b] = 1

grid[start_y][start_x+k+2] = 2

display()

d = S

def update(d):
    global y,x
    # drop tail if not apple
    if grid[y+d[0]][x+d[1]] != 2:
        grid[snake[0][0]][snake[0][1]] = 0
        snake.pop(0)
    # create apple if apple
    elif grid[y+d[0]][x+d[1]] == 2:
        apple_y,apple_x = random.choice([(y,x) for x in range(n) for y in range(n) if grid[y][x] == 0])
        grid[apple_y][apple_x] = 2

    y += d[0]
    x += d[1]

    snake.append([y,x])
     
    grid[y][x] = 1

    
    os.system('clear')
    display()


    time.sleep(0.01)


# ====================================================================================================

# gameplay
input()

def hamiltonian_cycle():
    global d
    while True:
        if x not in (0,n-1):
            if y == 1:
                if x % 2 == 1: d = E 
                else: d = S
            elif y == n-1:
                if x % 2 == 1: d = N 
                else: d = E
        if [y,x] == [0,0]: d = S
        if [y,x] == [n-1,0]: d = E
        if [y,x] == [n-1,n-1]: d = N
        if [y,x] == [0,n-1]: d = W

        update(d)
        if len(snake) == n*n-1:
            break

hamiltonian_cycle()

print('victory')
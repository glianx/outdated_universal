import random
import time
import os
os.system('clear')

def display():
    for row in grid:
        for node in row:
            print(['⬛','🟩','🟥'][node], end = '')
        print()

n = 15
grid = [[0 for x in range(n)] for y in range(n)]

N,E,S,W = [-1,0],[0,1],[1,0],[0,-1]

start_y,start_x = 5,2
k = 5

snake = [[start_y,start_x+i] for i in range(k)]

# snake head pos
y,x = start_y,start_x+k-1

for [a,b] in snake:
    grid[a][b] = 1

apple_y,apple_x = start_y,n-5
grid[start_y][n-5] = 2

display()

d = N

def update(d):
    global y,x
    global apple_y,apple_x
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


    # time.sleep(.1)


# ====================================================================================================

# gameplay


def direction():
    delta_y = apple_y - y 
    delta_x = apple_x - x
    deltas = [delta_y,delta_x]
    i = [abs(delta_y),abs(delta_x)].index(max(abs(delta_y),abs(delta_x)))
    direction = [0,0]
    if deltas[i] > 0: direction[i] = 1
    else: direction[i] = -1
    return direction

input()
while True:
    d = direction()
    if d == N and y > 0 and (grid[y-1][x] != 1 or [y-1,x] == snake[0]):
        update(d)
    elif d == S and y < n-1 and (grid[y+1][x] != 1 or [y+1,x] == snake[0]):
        update(d)
    elif d == E and x < n-1 and (grid[y][x+1] != 1 or [y,x+1] == snake[0]):
        update(d)
    elif d == W and x > 0 and (grid[y][x-1] != 1 or [y,x-1] == snake[0]): 
        update(d)
    else:
        break
    time.sleep(0.1)

print('You Lose')

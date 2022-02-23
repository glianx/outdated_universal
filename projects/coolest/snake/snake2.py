import random
import time
import os
os.system('clear')

def display():
    for row in grid:
        for node in row:
            print(['⬛','🟩','🟥'][node], end = '')
        print()

n = 12
grid = [[0 for x in range(n)] for y in range(n)]

N,E,S,W = [-1,0],[0,1],[1,0],[0,-1]

start_y,start_x = 5,2
k = 5

snake = [[start_y,start_x+i] for i in range(k)]

# snake head pos
y,x = start_y,start_x+k-1

for [a,b] in snake:
    grid[a][b] = 1

grid[start_y][n-3] = 2

display()
# time.sleep(.5)

d = N

def update(d):
    global y,x
    # pop tail if not apple
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

import readchar



import threading 
import time

def taskA():
    while True:
        update(d)
        time.sleep(.3)

def taskB():
    pass
    # c = readchar.readchar()
    # if c == 'a':
    #     d = W
    # taskB()

p1 = threading.Thread(target=taskA)
p2 = threading.Thread(target=taskB)

p1.start()
p2.start()

# def taskB():
#     getch = _Getch()()
#     if getch == 'f':
#         print(True)

# def taskB():
#     c = input_char()
#     if c == 'a':
#         d = W
#     elif c == 's':
#         d = S
#     taskB()

# def taskB():
#     global d
#     input_ = input()
#     if input_ == 'w':
#         d = N
#     elif input_ == 'a':
#         d = W
#     elif input_ == 's':
#         d = S
#     elif input_ == 'd':
#         d = E

#     taskB()

# def taskB():
#     input_ = _Getch()()

# def taskB(): 
#     pass

# def taskB():
#     global d
#     input_ = _Getch()() 
#     if input_ == '\x1b[A':
#         d = N 
#     elif input_ == '\x1b[B':
#         d = S
#     elif input_ == '\x1b[C':
#         d = E
#     elif input_ == '\x1b[D': 
#         d = W

#     taskB()

# def taskB():
#     global d

#     input_ = _Getch()() 

#     if input_ == '\x1b[A' and y > 0 and (grid[y-1][x] != 1 or [y-1,x] == snake[0]):
#         d = N 
#     elif input_ == '\x1b[B' and y < n-1 and (grid[y+1][x] != 1 or [y+1,x] == snake[0]):
#         d = S
#     elif input_ == '\x1b[C' and x < n-1 and (grid[y][x+1] != 1 or [y,x+1] == snake[0]):
#         d = E
#     elif input_ == '\x1b[D' and x > 0 and (grid[y][x-1] != 1 or [y,x-1] == snake[0]): 
#         d = W
#     # else:
#     #     print('You Lose')
#     #     exit()

#     taskB()


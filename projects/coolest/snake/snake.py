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
while True:
    input_ = _Getch()() 
    # print(input_,type(input_),len(input_))
    # if input_ not in ('\x1b[A','\x1b[B','\x1b[C','\x1b[D'):
    #     update_snake(d)
    #     continue
    if input_ == '\x1b[A' and y > 0 and (grid[y-1][x] != 1 or [y-1,x] == snake[0]):
        d = N 
        # update(d)
    elif input_ == '\x1b[B' and y < n-1 and (grid[y+1][x] != 1 or [y+1,x] == snake[0]):
        d = S
        # update(d)
    elif input_ == '\x1b[C' and x < n-1 and (grid[y][x+1] != 1 or [y,x+1] == snake[0]):
        d = E
        # update(d)
    elif input_ == '\x1b[D' and x > 0 and (grid[y][x-1] != 1 or [y,x-1] == snake[0]): 
        d = W
        # update(d)
    else:
        break
    update(d)

# while True:
#     time.sleep(0.1)
#     update(d)

print('You Lose')
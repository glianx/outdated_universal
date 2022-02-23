import random
import time
import os
os.system('clear')

n = 12

N,E,S,W = [-1,0],[0,1],[1,0],[0,-1]

start_y,start_x = 5,2
k = 5

snake = [[start_y,start_x+i] for i in range(k)]

# snake head pos
y,x = start_y,start_x+k-1

apple_yx = [start_y,start_x+k+2]

d = S

def display():
    for y in range(n):
        for x in range(n):
            if [y,x] in snake: print('🟩', end = '')
            elif [y,x] == apple_yx: print('🟥', end = '')
            else: print('  ', end = '')
        print()

def update(d):
    global y,x,apple_yx
    if [y+d[0],x+d[1]] == apple_yx:
        apple_yx = random.choice([[y,x] for x in range(n) for y in range(n) if [y,x] not in snake])
    else:
        snake.pop(0)

    y += d[0]
    x += d[1]

    snake.append([y,x])
     
    os.system('clear')
    display()

    time.sleep(0.01)

# ====================================================================================================

display()
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
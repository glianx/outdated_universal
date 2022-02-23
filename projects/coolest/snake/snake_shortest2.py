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

app_y,app_x = [start_y,start_x+k+2]

d = S

def display():
    for y in range(n):
        for x in range(n):
            if [y,x] in snake: print('🟩', end = '')
            elif [y,x] == [app_y,app_x]: print('🟥', end = '')
            else: print('  ', end = '')
        print()

def update(d):
    global y,x,app_y,app_x
    if [y+d[0],x+d[1]] == [app_y,app_x]:
        app_y,app_x = random.choice([[y,x] for x in range(n) for y in range(n) if [y,x] not in snake])
    else:
        snake.pop(0)

    y += d[0]
    x += d[1]

    snake.append([y,x])
     
    os.system('clear')
    display()

    time.sleep(0.02)
    # input()

# ====================================================================================================

display()
input()

def d(y,x,app_y,app_x):
    ds = []
    if abs(app_y-y) >= abs(app_x-x):
        if app_y - y > 0 : ds.append(S)
        elif app_y - y < 0: ds.append(N)
    elif abs(app_x-x) > abs(app_y-y):
        if app_x - x > 0: ds.append(E)
        elif app_x - x < 0: ds.append(W)
    d = ds[0]
    update(d)

while True:
    d(y,x,app_y,app_x)

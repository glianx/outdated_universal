import random
import time
import os
os.system('clear')
import icecream
from icecream import ic
n = 18

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
            if [y,x] in snake:
                if [y,x] == snake[-1]: print('🟦', end = '')
                elif [y,x] == snake[0]: print('🟧', end = '')
                else: print('🟩', end = '')
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
    # ic(y,x,app_y,app_x,abs(app_y-y),abs(app_x-x),app_y-y,app_x-x)
    # print(snake,app_y,app_x)
    # input()
    # print(len(snake))
    # time.sleep(0.02)
    input()



# ====================================================================================================

display()
input()

def shortest_path(y,x,app_y,app_x):
    global d
    ds = []
    # if abs(app_y-y) >= abs(app_x-x):
    #     if app_y - y > 0 : d = S
    #     elif app_y - y < 0: d = N
    # elif abs(app_x-x) > abs(app_y-y):
    #     if app_x - x > 0: d = E
    #     elif app_x - x < 0: d = W
    if abs(app_y-y) >= abs(app_x-x):
        if app_y - y >= 0 : ds.append(S)
        elif app_y - y < 0: ds.append(N)

        if app_x - x >= 0: ds.append(E)
        elif app_x - x < 0: ds.append(W)

    elif abs(app_x-x) > abs(app_y-y):
        if app_x - x > 0: ds.append(E)
        elif app_x - x < 0: ds.append(W)

        if app_y - y >= 0 : ds.append(S)
        elif app_y - y < 0: ds.append(N)

    remaining = [x for x in [N,S,E,W] if x not in ds]
    ds.extend(remaining)

    for i in range(3):
        # if i == 4: 
        #     print('you lose')
        #     break
        if [y+ds[i][0],x+ds[i][1]] not in snake and 0 <= y+ds[i][0] <= n-1 and 0 <= x+ds[i][1] <= n-1:
            d = ds[i]
            update(d)  
            break  

    # if [y+ds[0][0],x+ds[0][1]] not in snake and 0 <= y+ds[0][0] <= n-1 and 0 <= x+ds[0][1] <= n-1:
    #     d = ds[0]
    #     update(d)

    # elif [y+ds[1][0],x+ds[1][1]] not in snake and 0 <= y+ds[1][0] <= n-1 and 0 <= x+ds[1][1] <= n-1:
    #     d = ds[1]
    #     update(d)

    # else:
    #     for d in random.sample([x for x in [N,S,E,W] if x not in ds]):
    #         update(d)


while True:
    shortest_path(y,x,app_y,app_x)
print('you lose')


import random
import os
import time

n = 21
grid = [[1 for x in range(n)] for y in range(n)]

start_y,start_x = 0,0
end_y,end_x = n-1,n-1

grid[start_y][start_x] = 4
grid[end_y][end_x] = 5

def display_row(row):
    for node in row:
        print(['⬜','  ','🟥','🟩','🟦','🟦'][node], end = '')
    print()

def around_nodes(y,x):
    arounds = [[y,x+2],[y+2,x]]
    return [[a,b] for [a,b] in arounds if 0 <= a <= n-1 and 0 <= b <= n-1]

def visit_wall_between(y1,x1,y2,x2):
    grid[int((y1+y2)/2)][int((x1+x2)/2)] = 0

def binary_tree():
    for y in range(n):
        for x in range(0,n,2):
            if y % 2 == 0:
                if (y,x) != (end_y,end_x):
                    y2,x2 = random.choice(around_nodes(y,x))

                    if grid[y][x] == 1:
                        grid[y][x] = 0
                    if grid[y2][x2] == 1:
                        grid[y2][x2] = 0
                        
                    visit_wall_between(y2,x2,y,x)
        display_row(grid[y])
        time.sleep(0.01)
        
input()

start = time.time()  

binary_tree()

print(time.time() - start)


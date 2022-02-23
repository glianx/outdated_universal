import random
import os
import time

n = 21
grid = [[1 for x in range(n)] for y in range(n)]

start_y,start_x = 0,0
end_y,end_x = n-1,n-1

grid[start_y][start_x] = 4
grid[end_y][end_x] = 5

def display():
    os.system('clear')
    for row in grid:
        for node in row: 
            print('⬜⬛🟥🟩🟦🟦'[node], end = '')
        print()

def around_nodes(y,x):
    arounds = [[y-2,x],[y,x-2],[y,x+2],[y+2,x]]
    return [[a,b] for [a,b] in arounds if 0 <= a <= n-1 and 0 <= b <= n-1]

def visit_wall_between(y1,x1,y2,x2):
    grid[int((y1+y2)/2)][int((x1+x2)/2)] = 0

def random_dfs(y,x,prev_y,prev_x):
    if grid[y][x] in (1,5):
        
        grid[y][x] = 0
        visit_wall_between(y,x,prev_y,prev_x)

        display()

        for [new_y,new_x] in random.sample(around_nodes(y,x),len(around_nodes(y,x))):
            random_dfs(new_y,new_x,y,x)
        
display()
input()

(y,x) = random.choice([(0,2),(2,0)])

start = time.time()  

random_dfs(y,x,0,0)

print(time.time() - start)

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
    for row in grid:
        for node in row: 
            print(['⬜','  ','🟥','🟩','🟦','🟦'][node], end = '')
        print()

def visit_wall_between(y1,x1,y2,x2):
    grid[int((y1+y2)/2)][int((x1+x2)/2)] = 0

all_rows = []
drop_row = [0 for x in range(n)]

for y in range(0,n,2):
    # first colour all white
    for x in range(0,n,2):
        grid[y][x] = 0

    # create row of sets/types
    row = []
    for x in range(n):
        if x % 2 == 0: 
            if drop_row[x] != 0: # dropped from above
                row.append(drop_row[x])
            elif x == 0: # create new type for 1st node
                row.append(max(drop_row) + 2)
            elif x != 0: # create new type for remaining nodes
                row.append(max(row + drop_row) + 2)
        elif x % 2 == 1:
            row.append(-1)

    all_rows.append(row)

    # merge adjacent nodes not in same set
    for x in range(0,n-2,2):
        if row[x] != row[x+2] and random.choice((0,1)) == 1:
            # change all nodes of type row[x+2] to type row[x]
            k,l = row[x+2],row[x]
            for i in range(0,n-2,2):
                if row[i] == k:
                    row[i] = l
            grid[y][x+1] = 0

    # create drops / vertical connections
    if y <= n-2:
        drop_type = []
        drop_xs = []

        for x in range(0,n,2):
            if row[x] not in drop_type:
                drop_choices = [i for i in range(len(row)) if row[i] == row[x]]
                drop_x = random.choice(drop_choices)
                
                grid[y+1][drop_x] = 0
                grid[y+2][drop_x] = 0
                
                drop_type.append(row[x])
                drop_xs.append(drop_x)

                for x in drop_choices:
                    if random.choice((0,1)) == 1:
                        grid[y+1][x] = 0
                        grid[y+2][x] = 0
                        
                        drop_xs.append(x)

        drop_row  = [0 for x in range(n)]
        for x in drop_xs:
            drop_row[x] = row[x]

# last row 
for x in range(0,n,2):
    grid[n-1][x] = 0

for x in range(0,n-2,2):
    if drop_row[x] != drop_row[x+2] or [drop_row[x],drop_row[x+2]] == [1,1]:
        grid[n-1][x+1] = 0

display()

for row in all_rows:
    print(row)

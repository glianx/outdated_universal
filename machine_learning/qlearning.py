n = 10
grid = [[0 for x in range(n)] for y in range(n)]
grid[0][0] = 2
grid[-1][-1] = 3

print(grid)
def display():
    for row in grid:
        for value in row:
            print(['⬜️','🟦','🟥','🟩'][value],end = '')
        print()
display()
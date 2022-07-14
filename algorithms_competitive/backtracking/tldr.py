# all paths from top left to down right of an mXn matrix
# formulated algorithm and wrote code with minimal reference!

def print_path(path):
    for [cell_x, cell_y] in path:
        print(mat[cell_y][cell_x], end = ' ')
    print()
        
def tldr(mat, cell_x, cell_y, path):
    # matrix dimensions exceeded - out of bounds
    if cell_x > max_x or cell_y > max_y:
        return
    # matrix destination found
    if cell_x == max_x and cell_y == max_y:
        print_path(path)
        return
    tldr(mat, cell_x, cell_y + 1, path + [[cell_x, cell_y + 1]])
    tldr(mat, cell_x + 1, cell_y, path + [[cell_x + 1, cell_y]])

mat = [[1,2,3,4,5],
       [6,7,8,9,10],
       [11,12,13,14,15]]

max_x, max_y = len(mat[0]) - 1, len(mat) - 1
root_x, root_y = 0,0
path = [[root_x, root_y]]
tldr(mat, root_x, root_y, path)
def rotate(c):
    # c = [c[-1]] + c[:-1] # new_c unchanged
    # c[:] = [c[-1]] + c[:-1] # new_c changed
    c = [c[-1]] + c[:-1]
    # c[0],c[1] = c[1],c[0] # new_c changed
    print()

def bfs(c):
    # global new_c
    new_c = u2_r_f2.copy()
    rotate(new_c)
    print()


u2_r_f2 = [[0, 0, 4, 2, 5, 5, 4, 0, 0], [3, 3, 3, 3, 3, 1, 1, 1, 1], [5, 2, 2, 2, 4, 4, 5, 5, 2], [1, 3, 1, 1, 1, 3, 3, 1, 3], [0, 2, 2, 4, 4, 4, 0, 0, 4], [2, 0, 0, 4, 2, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6, 6, 6, 6]]

bfs('hello')
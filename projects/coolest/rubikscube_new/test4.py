def rotate(c,f):
    pass
    # c[f][0:8] = c[f][6:8] + c[f][0:6]
    # c[0] = c[1]

# def u(c):
#     rotate(c,0)
#     c[1][0:3],c[2][0:3],c[3][0:3],c[4][0:3] = c[2][0:3],c[3][0:3],c[4][0:3],c[1][0:3]

def bfs(c):
    new_c = u2_r_f2.copy()
    # new_c[0][:] = new_c[1][:]
    # new_c[0][0] = new_c[1][0]
    # new_c[0][2] = new_c[0][3]
    # new_c[0] = new_c[1]
    # new_c[0],new_c[1] = new_c[1],new_c[0]
    new_c[0][0],new_c[1][0] = new_c[1][0],new_c[0][0]

    # new_c[0][0:8] = new_c[0][6:8] + new_c[0][0:6]
    print()

u2_r_f2 = [[0, 0, 4, 2, 5, 5, 4, 0, 0], [3, 3, 3, 3, 3, 1, 1, 1, 1], [5, 2, 2, 2, 4, 4, 5, 5, 2], [1, 3, 1, 1, 1, 3, 3, 1, 3], [0, 2, 2, 4, 4, 4, 0, 0, 4], [2, 0, 0, 4, 2, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6, 6, 6, 6]]
bfs('hello')

import os
import time

def rotate(c,f):
    c[f][0:8] = c[f][6:8] + c[f][0:6]
def rotate_cc(c,f):
    c[f][0:8] = c[f][2:8] + c[f][0:2]
def rotate2(c,f):
    c[f][0:8] = c[f][4:8] + c[f][0:4]

def u(c):
    rotate(c,0)
    c[1][0:3],c[2][0:3],c[3][0:3],c[4][0:3] = c[2][0:3],c[3][0:3],c[4][0:3],c[1][0:3]
def d(c):
    rotate(c,5)
    c[4][4:7],c[3][4:7],c[2][4:7],c[1][4:7] = c[3][4:7],c[2][4:7],c[1][4:7],c[4][4:7]
def f(c):
    rotate(c,2)
    c[0][4:7],c[1][2:5],c[5][0:3],[c[3][6],c[3][7],c[3][0]] = c[1][2:5],c[5][0:3],[c[3][6],c[3][7],c[3][0]],c[0][4:7]
def b(c):
    rotate(c,4)
    c[0][0:3],c[3][2:5],c[5][4:7],[c[1][6],c[1][7],c[1][0]] = c[3][2:5],c[5][4:7],[c[1][6],c[1][7],c[1][0]],c[0][0:3]
def r(c):
    rotate(c,3)
    c[0][2:5],c[2][2:5],c[5][2:5],[c[4][6],c[4][7],c[4][0]] = c[2][2:5],c[5][2:5],[c[4][6],c[4][7],c[4][0]],c[0][2:5] 
def l(c):
    rotate(c,1)
    [c[0][6],c[0][7],c[0][0]],c[4][2:5],[c[5][6],c[5][7],c[5][0]],[c[2][6],c[2][7],c[2][0]] \
    = c[4][2:5],[c[5][6],c[5][7],c[5][0]],[c[2][6],c[2][7],c[2][0]],[c[0][6],c[0][7],c[0][0]]

def ui(c):
    rotate_cc(c,0)
    c[1][0:3],c[2][0:3],c[3][0:3],c[4][0:3] = c[4][0:3],c[1][0:3],c[2][0:3],c[3][0:3]
def di(c):
    rotate_cc(c,5)
    c[4][4:7],c[3][4:7],c[2][4:7],c[1][4:7] = c[1][4:7],c[4][4:7],c[3][4:7],c[2][4:7]
def fi(c):
    rotate_cc(c,2)
    c[0][4:7],c[1][2:5],c[5][0:3],[c[3][6],c[3][7],c[3][0]] = [c[3][6],c[3][7],c[3][0]],c[0][4:7],c[1][2:5],c[5][0:3]
def bi(c):
    rotate_cc(c,4)
    c[0][0:3],c[3][2:5],c[5][4:7],[c[1][6],c[1][7],c[1][0]] = [c[1][6],c[1][7],c[1][0]],c[0][0:3],c[3][2:5],c[5][4:7]
def ri(c):
    rotate_cc(c,3)
    c[0][2:5],c[2][2:5],c[5][2:5],[c[4][6],c[4][7],c[4][0]] = [c[4][6],c[4][7],c[4][0]],c[0][2:5] ,c[2][2:5],c[5][2:5]
def li(c):
    rotate_cc(c,1)
    [c[0][6],c[0][7],c[0][0]],c[4][2:5],[c[5][6],c[5][7],c[5][0]],[c[2][6],c[2][7],c[2][0]] \
    = [c[2][6],c[2][7],c[2][0]],[c[0][6],c[0][7],c[0][0]],c[4][2:5],[c[5][6],c[5][7],c[5][0]]

def u2(c):
    rotate2(c,0)
    c[1][0:3],c[2][0:3],c[3][0:3],c[4][0:3] = c[3][0:3],c[4][0:3],c[1][0:3],c[2][0:3]
def d2(c):
    rotate2(c,5)
    c[4][4:7],c[3][4:7],c[2][4:7],c[1][4:7] = c[2][4:7],c[1][4:7],c[4][4:7],c[3][4:7]
def f2(c):
    rotate2(c,2)
    c[0][4:7],c[1][2:5],c[5][0:3],[c[3][6],c[3][7],c[3][0]] = c[5][0:3],[c[3][6],c[3][7],c[3][0]],c[0][4:7],c[1][2:5]
def b2(c):
    rotate2(c,4)
    c[0][0:3],c[3][2:5],c[5][4:7],[c[1][6],c[1][7],c[1][0]] = c[5][4:7],[c[1][6],c[1][7],c[1][0]],c[0][0:3],c[3][2:5]
def r2(c):
    rotate2(c,3)
    c[0][2:5],c[2][2:5],c[5][2:5],[c[4][6],c[4][7],c[4][0]] = c[5][2:5],[c[4][6],c[4][7],c[4][0]],c[0][2:5],c[2][2:5]
def l2(c):
    rotate2(c,1)
    [c[0][6],c[0][7],c[0][0]],c[4][2:5],[c[5][6],c[5][7],c[5][0]],[c[2][6],c[2][7],c[2][0]] \
    = [c[5][6],c[5][7],c[5][0]],[c[2][6],c[2][7],c[2][0]],[c[0][6],c[0][7],c[0][0]],c[4][2:5]

def exec_m(c,exec_moves):
    for move in exec_moves:
        if move == 'u': u(c)
        if move == "ui": ui(c)
        if move == 'u2': u2(c)
        if move == 'r': r(c)
        if move == "ri": ri(c)
        if move == 'r2': r2(c)
        if move == 'l': l(c)
        if move == "li": li(c)
        if move == 'l2': l2(c)
        if move == 'f': f(c)
        if move == "fi": fi(c)
        if move == 'f2': f2(c)
        if move == 'd': d(c)
        if move == "di": di(c)
        if move == 'd2': d2(c)
        if move == 'b': b(c)
        if move == "bi": bi(c)
        if move == 'b2': b2(c)

def input_moves(c):
    while True:
        render(c)
        print(c)
        inp = input()
        if inp == '':
            break
        else:
            eval(inp + '(c)')

def render(c):
    # os.system('clear')
    for facerow in [[-1,0],[1,2,3,4],[-1,5]]:
        for row in [[0,1,2],[7,8,3],[6,5,4]]:
            for face in facerow:
                for sticker in row:
                    print(colrs[c[face][sticker]],end = '')
            print()

def cross_solved(c):
    return [c[5][1],c[5][3],c[5][5],c[5][7]] == [5,5,5,5] and [c[1][5],c[2][5],c[3][5],c[4][5]] == [1,2,3,4]

def bfs():
    ctr = 0
    for _states in range(18+18**2+18**3+18**4+18**5):
        ctr += 1
        # new_c = [[-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, 1, -1, -1, -1, -1, -1, -1, -1], [-1, 4, -1, -1, -1, 2, -1, -1, -1], [-1, -1, -1, -1, -1, 3, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1]]
        # OG 
        new_c = [[-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, 1, -1, -1, -1], [-1, -1, -1, -1, -1, 2, -1, -1, -1], [-1, -1, -1, -1, -1, 3, -1, -1, -1], [-1, -1, -1, -1, -1, 4, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1]]
        exec_m(new_c,scramble_moves)

        state = Q.pop(0)
        exec_m(new_c,state)
        # print(state)

        if new_c == [[-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, 1, -1, -1, -1], [-1, -1, -1, -1, -1, 2, -1, -1, -1], [-1, -1, -1, -1, -1, 3, -1, -1, -1], [-1, -1, -1, -1, -1, 4, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1]]:
            render(new_c)
            print(state)
            print(ctr)
            break

        if len(state) < 5:
            for next_move in moves:
                if next_move[0][0] != state[-1][0]:
                    if [state[-1][0],next_move[0][0]] not in dupl_opp_faces:
                        next_state = state + next_move
                        Q.append(next_state)

moves = [['u'] ,['d'], ['l'], ['r'], ['f'], ['b'],
         ['ui'],['di'],['li'],['ri'],['fi'],['bi'],
         ['u2'],['d2'],['l2'],['r2'],['f2'],['b2']]

Q = moves.copy()


colrs = ['🟨','🟧','🟦','🟥','🟩','⬜️','  ']
dupl_opp_faces = [['d','u'],['r','l'],['b','f']]

rc = [[col_i for _sticker in range(9)] for col_i in range(7)]
cc = [[-1 for _sticker in range(9)] for col_i in range(7)]
cc[1][5],cc[2][5],cc[3][5],cc[4][5] = 1,2,3,4

scramble_moves = ['ri','l2','u','b2']

# start = time.time()
bfs()
# print(time.time()-start)
from audioop import cross
import os
import time
import random

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

def render_scrambled():
    display_c = [[col_i for _sticker in range(9)] for col_i in range(7)]
    exec_m(display_c,scramble_moves)
    render(display_c)
    print(scramble_moves)
    print(reverse_moves(scramble_moves))
    input()

def render_solution(c,state,start):
    print(time.time() - start)
    render(c)
    print('state',state)
    print('undo:',reverse_moves(state))
    input('DONE')

def cross_solved(c):
    return [c[5][1],c[5][3],c[5][5],c[5][7]] == [5,5,5,5] and [c[1][5],c[2][5],c[3][5],c[4][5]] == [1,2,3,4]

def f2l_pair(c,i):
    cc_face = [None,2,3,4,1]
    for _urotation in range(4):
        winter_left = [c[0][3],c[0][4],c[3][0],c[3][1],c[2][2]]
        winter_right = [c[4][1],c[4][2],c[0][0],c[0][1],c[1][0]]
        summer_left = [c[0][6],c[4][1],c[0][1],c[2][0],c[1][2]]
        summer_right = [c[2][2],c[0][1],c[0][4],c[4][1],c[3][0]]
        if [i,i,cc_face[i],cc_face[i],5] in [winter_left,winter_right,summer_left,summer_right]:
            return True
        exec_m(c,['u'])
    return False

def reverse_moves(moves):
    reversed_moves = list(reversed(moves))
    for i in range(len(reversed_moves)):
        if len(reversed_moves[i]) == 1: 
            reversed_moves[i] += 'i'
        elif reversed_moves[i][1] == 'i':
            reversed_moves[i] = reversed_moves[i][0]
    return reversed_moves

def bfs(stage,Q,state=None,pair=None):
    render_scrambled()
    start = time.time()
    len_state = 1
    state_start = 'u'
    prev_time = 0

    for _states in range(18+18**2+18**3+18**4+18**5+18**6+18**7+18**8):
        if Q == []: 
            break

        new_c = [[col_i for _sticker in range(9)] for col_i in range(7)]
        exec_m(new_c,scramble_moves)
        if stage != 'cross': exec_m(new_c,state)

        state = Q.pop(0)
        exec_m(new_c,state)

        if len(state) > len_state:
            print(len(state), time.time() - start)
            len_state = len(state)
        if state[0] != state_start:
            print('\t',state[0], time.time() - start,'\t',time.time() - prev_time)
            prev_time = time.time()
            state_start = state[0]

        if stage == 'cross':
            if cross_solved(new_c):
                print(stage)
                render_solution(new_c,state,start)
                bfs('f2l',Q,state,pair = 0)
        elif stage == 'f2l':
            if cross_solved(new_c):
                if f2l_pair(new_c,pair):
                    print(f2l_pair(new_c,pair),pair)
                    render_solution(new_c,state,start)
                    print(stage)

        if len(state) < 4:
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

# scramble_moves = sum([random.choice(moves) for i in range(5)],[])
scramble_moves = ['r2','u2','d','f2']

Q = moves.copy()
bfs('cross',Q)

# moves = ['b','u','b2','l']
# exec_m(rc,moves)
# render(rc)
# for i in range(1,5):
#     print(f2l_pair(rc,i))
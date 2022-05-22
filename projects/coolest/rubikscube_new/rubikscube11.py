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

def m(c):
    c[0][1],c[0][5],c[0][8], c[2][1],c[2][5],c[2][8], c[5][1],c[5][5],c[5][8], c[4][5],c[4][1],c[4][8] \
    = c[4][5],c[4][1],c[4][8], c[0][1],c[0][5],c[0][8], c[2][1],c[2][5],c[2][8], c[5][1],c[5][5],c[5][8]
def mi(c):
    c[0][1],c[0][5],c[0][8], c[2][1],c[2][5],c[2][8], c[5][1],c[5][5],c[5][8], c[4][5],c[4][1],c[4][8] \
    = c[2][1],c[2][5],c[2][8], c[5][1],c[5][5],c[5][8], c[4][5],c[4][1],c[4][8], c[0][1],c[0][5],c[0][8]
def m2(c):
    c[0][1],c[0][5],c[0][8], c[2][1],c[2][5],c[2][8], c[5][1],c[5][5],c[5][8], c[4][5],c[4][1],c[4][8] \
    = c[5][1],c[5][5],c[5][8], c[4][5],c[4][1],c[4][8], c[0][1],c[0][5],c[0][8], c[2][1],c[2][5],c[2][8]

def L(c):
    l(c)
    m(c)
def Li(c):
    li(c)
    mi(c)
def R(c):
    r(c)
    mi(c)
def Ri(c):
    ri(c)
    m(c)
def R2(c):
    R(c)
    R(c)

def x(c):
    c[0],c[2],c[5],c[4] = c[2],c[5],c[4][4:8]+c[4][0:4]+[c[4][8]],c[0][4:8]+c[0][0:4]+[c[0][8]]
    rotate(c,3)
    rotate_cc(c,1)

def xi(c):
    c[0],c[2],c[5],c[4] = c[4][4:8]+c[4][0:4]+[c[4][8]],c[0],c[2],c[5][4:8]+c[5][0:4]+[c[5][8]]
    rotate_cc(c,3)
    rotate(c,1)

def y(c):
    c[1],c[2],c[3],c[4] = c[2],c[3],c[4],c[1]
    rotate(c,0)
    rotate_cc(c,5)

def none_move(c):
    pass

def exec_m(c,exec_moves):
    for move in exec_moves:
        eval(move + '(c)')

def input_moves(c):
    while True:
        render(c)
        print(c)
        inp = input()
        if inp == '':
            break
        else:
            exec(inp)

def render(c):
    # os.system('clear')
    for facerow in [[-1,0],[1,2,3,4],[-1,5]]:
        for row in [[0,1,2],[7,8,3],[6,5,4]]:
            for face in facerow:
                for sticker in row:
                    print(colrs[c[face][sticker]],end = '')
            print()

def render_solution(c,state,start):
    print(time.time() - start)
    render(c)
    print('state',state)
    print('undo:',reverse_moves(state))

def cross_solved(c):
    return [c[5][1],c[5][3],c[5][5],c[5][7]] == [5,5,5,5] and [c[1][5],c[2][5],c[3][5],c[4][5]] == [1,2,3,4]

def f2l_pair(c,i):
    cc_face = [None,2,3,4,1]
    for _urot in range(4):
        winter_left = [c[0][3],c[0][4],c[3][0],c[3][1],c[2][2]]
        winter_right = [c[4][1],c[4][2],c[0][0],c[0][1],c[1][0]]
        summer_left = [c[0][6],c[4][1],c[0][1],c[2][0],c[1][2]]
        summer_right = [c[2][2],c[0][1],c[0][4],c[4][1],c[3][0]]
        pos = [i,i,cc_face[i],cc_face[i],5]
        if pos in [winter_left,winter_right,summer_left,summer_right]:
            exec_m(c,['ui' for _ in range(_urot)])
            return True
        exec_m(c,['u'])
    return False

def f2l_slot(c,i):
    cc_face = [None,2,3,4,1]
    w_face = [None,0,2,4,6]
    pos = [i,i,cc_face[i],cc_face[i],5]
    if pos == [c[i][3],c[i][4],c[cc_face[i]][6],c[cc_face[i]][7],c[5][w_face[i]]]:
        return True
    exec_m(c,['u'])
    return False

def oll_solved(c):
    return c[0] == [0 for _ in range(9)]

def pll_solved(c):
    return [c[1][0:4],c[2][0:4],c[3][0:4],c[4][0:4]] == [[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]

def reverse_moves(moves):
    reversed_moves = list(reversed(moves))
    for i in range(len(reversed_moves)):
        if len(reversed_moves[i]) == 1: 
            reversed_moves[i] += 'i'
        elif reversed_moves[i][1] == 'i':
            reversed_moves[i] = reversed_moves[i][0]
    return reversed_moves

def bfs(stage,prev_state=[],i=None,):
    Q = [['none_move']] + moves.copy()
    start = time.time()
    len_state = 1
    state_start = 'u'
    prev_time = 0
    
    if stage in ['cross','pair','slot']: 
        for _states in range(18+18**2+18**3+18**4):
            if Q == []: 
                break

            new_c = [[col_i for _sticker in range(9)] for col_i in range(7)]
            exec_m(new_c,  scramble)
            if prev_state: exec_m(new_c,prev_state)

            state = Q.pop(0)
            exec_m(new_c,state)

            if len(state) > len_state:
                print(len(state), time.time() - start)
                len_state = len(state)
            if state[0] != state_start:
                print('\t',state[0], time.time() - start,'\t',time.time() - prev_time)
                prev_time = time.time()
                state_start = state[0]

            if cross_solved(new_c):
                if stage == 'cross':
                    render_solution(new_c,state,start)
                    if interactive: input('cross solved!')
                    return prev_state + state
                if stage == 'pair' and f2l_pair(new_c,i) and all([f2l_slot(new_c,j) for j in range(1,i)]) \
                or stage == 'slot' and f2l_slot(new_c,i) and all([f2l_slot(new_c,j) for j in range(1,i)]):
                    render_solution(new_c,state,start)
                    if interactive: input('f2l '+stage+' solved!')
                    return prev_state + state

            if state == ['none_move']: continue

            if len(state) < 4:
                for next_move in moves:
                    if next_move[0][0] != state[-1][0]:
                        if [state[-1][0],next_move[0][0]] not in dupl_opp_faces:
                            next_state = state + next_move
                            Q.append(next_state)

    elif stage in ['oll','pll']:
        algorithms = open(stage+'_algs.txt').read()
        algorithms = algorithms.split('\n')
        for i in range(len(algorithms)):
            algorithms[i] = algorithms[i].split()

        for urot in ['none_move','u','u2','ui']:
            for state in algorithms:

                new_c = [[col_i for _sticker in range(9)] for col_i in range(7)]
                exec_m(new_c,scramble)
                exec_m(new_c,prev_state)
                exec_m(new_c,[urot])

                exec_m(new_c,state)
                if eval(stage+'_solved(new_c)'):
                    render_solution(new_c,[urot] + state,start)
                    print(algorithms.index(state))
                    input(stage+' solved!')
                    return prev_state + [urot] + state

moves = [['u'] ,['d'], ['l'], ['r'], ['f'], ['b'],
         ['ui'],['di'],['li'],['ri'],['fi'],['bi'],
         ['u2'],['d2'],['l2'],['r2'],['f2'],['b2']]

colrs = ['🟨','🟧','🟦','🟥','🟩','⬜️','  ']
dupl_opp_faces = [['d','u'],['r','l'],['b','f']]

algs = [[]]

new_c = [[col_i for _sticker in range(9)] for col_i in range(7)]

# scramble = ['r2','u2','f','d']
# scramble = ['m','u','mi','u','R','u','Ri','u','Li','u','m2','u','mi','u']
scramble = "R u ri ui Ri r u r ui ri".split()
# scramble = ['r2','u2','f','d']

# scramble = algorithms[-1]

# exec_m(new_c,  scramble)
# render(new_c)
# print(scramble)
# print(reverse_moves(scramble))

# input()

interactive = False

prev_state = bfs('cross')
for i in range(1,5):
    prev_state = bfs('pair',prev_state,i)
    prev_state = bfs('slot',prev_state,i)
prev_state = bfs('oll',prev_state)
prev_state = bfs('pll',prev_state)
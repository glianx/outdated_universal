import random
import math
import time
import os
os.system('clear')

board = [[0 for x in range(3)] for y in range(3)]
board2 = [["⬜️" for x in range(3)] for y in range(3)]

def drawboard():
    for row in board2:
        for square in row:
            print(square, end = '')
        print()

def return_win_board():
    for row in board:
        if row[0] == row[1] == row[2]: return row[0]
    for x in range(3):
        if board[0][x] == board[1][x] == board[2][x]: return board[0][x]
    if board[1][1] == board[0][0] == board[2][2]: return board[1][1]
    if board[1][1] == board[0][2] == board[2][0]: return board[1][1]
    return 0

def update():
    os.system('clear')
    print()
    drawboard()
    print('winner:', return_win_board())
    if return_win_board() == 1:
        print('🎉 Congratulations! x wins!')
    if return_win_board() == -1:
        print('🎉 Congratulations! o wins!')

def xmove(x):
    board[x//3][x%3] = 1
    board2[x//3][x%3] = '❌'  
    update()

def omove(o):
    board[o//3][o%3] = -1
    board2[o//3][o%3] = '⭕️'  
    update()

drawboard()

minimax_list = []

def minimax(minmax, inputs, n):
    # min/max of n-sized chunks
    moves = [minmax(inputs[i:i+n]) for i in range(0,len(inputs),n)]
    minimax_list.append(moves)
    if minmax == min: minmax = max
    elif minmax == max: minmax = min
    if len(moves) > 1: minimax(minmax, moves, n+1)

def x(li):
    return [li[i] for i in range(len(li)) if i % 2 == 0]

def o(li): 
    return [li[i] for i in range(len(li)) if i % 2 == 1]

def return_win(x,o):
    x_win, o_win = False, False
    wins = [{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}]
    for win in wins:
        if win.issubset(set(x)): 
            x_win = True 
            x_win_set = win
        if win.issubset(set(o)): 
            o_win = True
            o_win_set = win
    if (x_win,o_win) == (True,False): return 1
    if (x_win,o_win) == (False,True): return -1
    if (x_win,o_win) == (True,True): 
        x_win_move = max([x.index(i) for i in x_win_set])
        o_win_move = max([o.index(i) for i in o_win_set])
        if x_win_move <= o_win_move: return 1
        elif o_win_move < x_win_move: return -1
    if (x_win,o_win) == (False,False): return 0

def return_ends(n):
    ends = []
    for a in range(n): 
        for b in range(n): 
            if b == a: continue
            for c in range(n):
                if c in (a,b): continue
                for d in range(n):
                    if d in (a,b,c): continue
                    for e in range(n):
                        if e in (a,b,c,d): continue
                        for f in range(n):
                            if f in (a,b,c,d,e): continue
                            for g in range(n):
                                if g in (a,b,c,d,e,f): continue
                                for h in range(n): 
                                    if h in (a,b,c,d,e,f,g): continue   
                                    for i in range(n):
                                        if i in (a,b,c,d,e,f,g,h): continue                   
                                        ends.append(return_win(x([a,b,c,d,e,f,g,h,i]),o([a,b,c,d,e,f,g,h,i])))
    return ends

start1 = time.time()

ends = return_ends(9)

print(time.time()-start1)

minimax(min,ends,2)
minimax_list.reverse()
minimax_list.pop(0)
minimax_list.append(ends)
# for i in minimax_list:
#     print(len(i))

# =====================================================

# xwins, owins = 0,0 

board = [[0 for x in range(3)] for y in range(3)]
board2 = [["⬜️" for x in range(3)] for y in range(3)]
blanks = [0,1,2,3,4,5,6,7,8]

opos = 1
n = 9
i = 1

while len(blanks) > 0:
    xy = input('x move: ')
    x = int(xy[0]) + 3 * int(xy[1])
    xmove(x)

    if n == 9: xpos = x
    else: xpos = n * opos + blanks.index(x)
    blanks.remove(x)
    n -= 1

    if return_win_board() or len(blanks) == 0: break

    o_range = minimax_list[i][n*xpos:n*xpos+n]
    # o = blanks[o_range.index(min(o_range))]
    o = random.choice([blanks[i] for i in range(len(blanks)) if o_range[i] == min(o_range)])
    omove(o)

    opos = n * xpos + blanks.index(o)

    blanks.remove(o)
    n -= 1
    i += 2

    if return_win_board() or len(blanks) == 0: break
    

if len(blanks) == 0:
    print('🤝 Draw!')





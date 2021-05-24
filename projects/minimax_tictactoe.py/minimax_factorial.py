import random
import math
import time
import os
os.system('clear')

minimax_list = []
def minimax(minmax, inputs, n):
    # min/max of n-sized chunks
    moves = [minmax(inputs[i:i+n]) for i in range(0,len(inputs),n)]
    move_chunks = [moves[i:i+n+1] for i in range(0, len(moves),n+1)]
    print(str(minmax)[-4:-1], len(moves), 'n:', n)
    if n > 3: print(move_chunks)
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

def final_digit_strings(n):
    strings = []
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
                                        strings.append([a,b,c,d,e,f,g,h,i])
    return strings

strings = final_digit_strings(9)

ends = []

for li in strings: 
    ends.append(return_win(x(li),o(li)))

minimax(min,ends,2)
minimax_list.reverse()
minimax_list.pop(0)
minimax_list.append(ends)
# print(len(minimax_list))
# for i in minimax_list:
#     print(len(i))

blanks = [0,1,2,3,4,5,6,7,8]

x0 = int(input('x move: '))
blanks.remove(x0)

o1range = minimax_list[1][8*x0:8*x0+8]
o1 = blanks[o1range.index(min(o1range))]
print(o1)
blanks.remove(o1)
o1pos = 8 * x0 + o1range.index(min(o1range))

x2 = int(input('x move: '))
x2pos = 7 * o1pos + blanks.index(x2)
blanks.remove(x2)

o3range = minimax_list[3][6*x2pos:6*x2pos+6]
o3 = blanks[o3range.index(min(o3range))]
print(o3)
blanks.remove(o3)
o3pos = 6 * x2pos + o3range.index(min(o3range))

x4 = int(input('x move: '))
x4pos = 5 * o3pos + blanks.index(x4)
blanks.remove(x4)

o5range = minimax_list[5][4*x4pos:4*x4pos+4]
o5 = blanks[o5range.index(min(o5range))]
print(o5)
blanks.remove(o5)
o5pos = 4 * x4pos + o5range.index(min(o5range))

x6 = int(input('x move: '))
x6pos = 3 * o5pos + blanks.index(x6)
blanks.remove(x6)

o7range = minimax_list[7][2*x6pos:2*x6pos+2]
o7 = blanks[o7range.index(min(o7range))]
print(o7)
blanks.remove(o7)

x8 = int(input('x move: '))
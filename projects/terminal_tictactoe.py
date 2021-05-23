import os
os.system('clear')
import random
import time

# 🟥🟧🟨🟩🟦🟪⬛️⬜️🟫
board = [[0 for x in range(3)] for y in range(3)]
board2 = [["⬜️" for x in range(3)] for y in range(3)]

def drawboard():
    for row in board2:
        for square in row:
            print(square, end = '')
        print()

drawboard()

def return_win():
    for row in board:
        if row[0] == row[1] == row[2]: return row[0]
    for x in range(3):
        if board[0][x] == board[1][x] == board[2][x]: return board[0][x]
    if board[1][1] == board[0][0] == board[2][2]: return board[1][1]
    if board[1][1] == board[0][2] == board[2][0]: return board[1][1]

def minimax():
    pass

while True:
    usermove = input('enter move: ')
    userx,usery = int(usermove[0]),int(usermove[1])
    while board[usery][userx]:
        usermove = input('enter move: ')
        userx,usery = int(usermove[0]),int(usermove[1])

    board[usery][userx] = 1
    board2[usery][userx] = '❌'  

    os.system('clear')
    drawboard()

    if return_win():
        print('you are winner:', return_win())
        print(board)
        break
    # time.sleep(.5)

    computerx, computery = random.randrange(3),random.randrange(3)
    while board[computery][computerx]:
        computerx, computery = random.randrange(3),random.randrange(3)

    board[computery][computerx] = -1
    board2[computery][computerx] = '⭕️'

    os.system('clear')
    drawboard()

    if return_win():
        print('computer is winner:', return_win())
        print(board)
        break

    
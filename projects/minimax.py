import random
end = [random.randrange(-10,10) for x in range(16)]
print('end', end)

def minimax(minmax, inputs):
    moves = []
    for i in range(0,int(len(inputs)),2):
        moves.append(minmax(inputs[i:i+2]))
    print(str(minmax)[-4:-1], moves)
    if minmax == min: minmax = max
    elif minmax == max: minmax = min
    if len(moves) > 1: minimax(minmax, moves)

minimax(min, end)

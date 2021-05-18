import random
inputs = [random.randrange(10) for x in range(16)]
print('end', inputs)

minmax = min
while len(inputs) > 1:
    moves = []
    for i in range(0,int(len(inputs)),2):
        moves.append(minmax(inputs[i:i+2]))
    print(str(minmax)[-4:-1], moves)
    if minmax == min: minmax = max
    elif minmax == max: minmax = min
    inputs = moves
    

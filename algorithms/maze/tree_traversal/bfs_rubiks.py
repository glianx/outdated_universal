moves = [['u'],['d'],['l'],['r'],['f'],['b']]

def bfs_queue():
    Q = [['u'],['d'],['l'],['r'],['f'],['b']]
    for i in range(6**2):
        state = Q.pop(0)
        for next_move in moves:
            print(state + next_move)
            Q.append(state + next_move)

bfs_queue()
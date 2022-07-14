moves = [['u'],['d'],['l'],['r'],['f'],['b'],
         ['ui'],['di'],['li'],['ri'],['fi'],['bi'],
         ['u2'],['d2'],['l2'],['r2'],['f2'],['b2']]

def bfs_queue():
    Q = [['u'],['d'],['l'],['r'],['f'],['b'],
         ['ui'],['di'],['li'],['ri'],['fi'],['bi'],
         ['u2'],['d2'],['l2'],['r2'],['f2'],['b2']]
    for i in range(6**2):
        state = Q.pop(0)
        print(state)
        for next_move in moves:
            Q.append(state + next_move)
    print(Q)

bfs_queue()
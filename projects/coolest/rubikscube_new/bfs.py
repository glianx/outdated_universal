import cube
    
def bfs():
    for _states in range(18):
        cube.c = cube.cc.copy()
        
        state = Q.pop(0)
        # print('cube.cc.copy():',cube.cc.copy())
        # c = cube.cc.copy()
        # print(c)

        for move in state:
            eval("cube." + move + '(cube.c)')
        
        cube.render(cube.c)
        # cube.render(c)
        # print(c)
        # print(cube.cc)
        print(state)

        # for next_move in moves:
        #     new_state = state + next_move
        #     Q.append(new_state)
  
# def bfs():
#     for _ in range(18):
#         state = Q.pop(0)
#         for move in state:
#             c = cc.copy()
#             eval("cube." + move + '()')
#             cube.render()
#             print(state)

#         for next_move in moves:
#             new_state = state + next_move
#             Q.append(new_state)
#             # print(new_state)
#     # print(Q)

moves = [['u'] ,['d'], ['l'], ['r'], ['f'], ['b'],
         ['ui'],['di'],['li'],['ri'],['fi'],['bi'],
         ['u2'],['d2'],['l2'],['r2'],['f2'],['b2']]

Q = moves.copy()

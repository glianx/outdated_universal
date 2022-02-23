def render(c):
    print()
    for facerow in [[c[-1],c[0]], c[1:5], [c[-1],c[5]]]:
        for row in range(3):
            for face in facerow:
                for col in range(3):
                    print(colrs[face[row][col]],end = '')
            print()

def rotate(f):
    c[f][0][0],c[f][0][2],c[f][2][2],c[f][2][0] = c[f][2][0],c[f][0][0],c[f][0][2],c[f][2][2]
    c[f][0][1],c[f][1][2],c[f][2][1],c[f][1][0] = c[f][1][0],c[f][0][1],c[f][1][2],c[f][2][1]

def u():
    rotate(0)
    c[1][0],c[2][0],c[3][0],c[4][0] = c[2][0],c[3][0],c[4][0],c[1][0]

def r():
    rotate(3)
    c[0][0][2],c[0][1][2],c[0][2][2],c[2][0][2],c[2][1][2],c[2][2][2],c[5][0][2],c[5][1][2],c[5][2][2],c[4][2][0],c[4][1][0],c[4][0][0] = c[2][0][2],c[2][1][2],c[2][2][2],c[5][0][2],c[5][1][2],c[5][2][2],c[4][2][0],c[4][1][0],c[4][0][0],c[0][0][2],c[0][1][2],c[0][2][2]

colr_ints = [0,1,2,3,4,5,6]
colrs = ['🟨','🟧','🟦','🟥','🟩','⬜️','  ']
c = [[[colr for x in range(3)] for y in range(3)] for colr in colr_ints]

render(c)
r()
u()
r()
u()
render(c)

print(c[0][0][:])
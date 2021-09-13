cube = [[x for _ in range(9)] for x in range(6)]
pixels = ['🟨','🟧','🟦','🟥','🟩','⬜️','  ']
blank_row = [6 for _ in range(3)]
blank_face = blank_row = [6 for _ in range(9)]

def render():
    for faces_row in [[blank_face,cube[0]],[cube[1],cube[2],cube[3],cube[4]],[blank_face,cube[5]]]:
        for row_stickers in [[0,1,2],[7,8,3],[6,5,4]]:
            for face in faces_row:
                for sticker_index in row_stickers:
                    print(pixels[face[sticker_index]],end = '')
            print()
    print()

def clockwise_move(face,edges,b):
    face.insert(0,face.pop(-2))
    face.insert(0,face.pop(-2))
    edges2 = edges.copy()
    for i in range(4):
        render()
        edges[i][:b] = edges2[i-1][:b]

    # edges[0][:b],edges[1][:b],edges[2][:b],edges[3][:b] = edges[3][:b],edges[0][:b],edges[1][:b],edges[2][:b]

def u():
    clockwise_move(cube[0],[cube[4],cube[3],cube[2],cube[1]],3)
    # clockwise_move(cube[0],[cube[1],cube[2],cube[3],cube[4]],3)


u()


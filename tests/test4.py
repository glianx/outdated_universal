import time

class Face:
    def __init__(self,colour):
        for sticker in ['ul','u','ur','l','m','r','dl','d','dr']:
            setattr(self,sticker,colour)
        self.face_loop = [self.ul,self.u,self.ur,self.r,self.dr,self.d,self.dl,self.l,self.m]
        self.face_row = [self.ul,self.u,self.ur,self.l,self.m,self.r,self.dl,self.d,self.dr]

    def clockwise(self):
        self.ul,self.l,self.dl,self.d,self.dr,self.r,self.ur,self.u = self.dl,self.d,self.dr,self.r,self.ur,self.u,self.ul,self.l

    def counterclockwise(self):
        self.ul,self.u,self.ur,self.r,self.dr,self.d,self.dl,self.l = self.ur,self.r,self.dr,self.d,self.dl,self.l,self.ul,self.u

def render():
    for face_row in [[blankface,uface],[lface,fface,rface,bface],[blankface,dface]]:
        for row_stickers in [['ul','u','ur'],['l','m','r'],['dl','d','dr']]:
            for face in face_row:
                for sticker_index in row_stickers:
                    print(pixels[getattr(face,sticker_index)],end = '')
            print()
    print()

def u():
    uface.clockwise()
    fface.ul,fface.u,fface.ur,rface.ul,rface.u,rface.ur,bface.ul,bface.u,bface.ur,lface.ul,lface.u,lface.ur = rface.ul,rface.u,rface.ur,bface.ul,bface.u,bface.ur,lface.ul,lface.u,lface.ur,fface.ul,fface.u,fface.ur

def r():
    rface.clockwise()
    uface.ur,uface.r,uface.dr,fface.ur,fface.r,fface.dr,dface.ur,dface.r,dface.dr,bface.dl,bface.l,bface.ul = fface.ur,fface.r,fface.dr,dface.ur,dface.r,dface.dr,bface.dl,bface.l,bface.ul,uface.ur,uface.r,uface.dr

def l():
    lface.clockwise()
    uface.ul,uface.l,uface.dl,bface.dr,bface.r,bface.ur,dface.ul,dface.l,dface.dl,fface.ul,fface.l,fface.dl = bface.dr,bface.r,bface.ur,dface.ul,dface.l,dface.dl,fface.ul,fface.l,fface.dl,uface.ul,uface.l,uface.dl

def f():
    fface.clockwise()
    uface.dl,uface.d,uface.dr,lface.dr,lface.r,lface.ur,dface.ur,dface.u,dface.ul,rface.ul,rface.l,rface.dl = lface.dr,lface.r,lface.ur,dface.ur,dface.u,dface.ul,rface.ul,rface.l,rface.dl,uface.dl,uface.d,uface.dr

def d():
    dface.clockwise()
    fface.dl,fface.d,fface.dr,lface.dl,lface.d,lface.dr,bface.dl,bface.d,bface.dr,rface.dl,rface.d,rface.dr = lface.dl,lface.d,lface.dr,bface.dl,bface.d,bface.dr,rface.dl,rface.d,rface.dr,fface.dl,fface.d,fface.dr

def b():
    bface.clockwise()
    uface.ur,uface.u,uface.ul,rface.dr,rface.r,rface.ur,dface.dl,dface.d,dface.dr,lface.ul,lface.l,lface.dl = rface.dr,rface.r,rface.ur,dface.dl,dface.d,dface.dr,lface.ul,lface.l,lface.dl,uface.ur,uface.u,uface.ul



def ui():
    uface.counterclockwise()
    fface.ul,fface.u,fface.ur,rface.ul,rface.u,rface.ur,bface.ul,bface.u,bface.ur,lface.ul,lface.u,lface.ur = lface.ul,lface.u,lface.ur,fface.ul,fface.u,fface.ur,rface.ul,rface.u,rface.ur,bface.ul,bface.u,bface.ur

def ri():
    rface.counterclockwise()
    uface.ur,uface.r,uface.dr,fface.ur,fface.r,fface.dr,dface.ur,dface.r,dface.dr,bface.dl,bface.l,bface.ul = bface.dl,bface.l,bface.ul,uface.ur,uface.r,uface.dr,fface.ur,fface.r,fface.dr,dface.ur,dface.r,dface.dr

def li():
    lface.counterclockwise()
    uface.ul,uface.l,uface.dl,bface.dr,bface.r,bface.ur,dface.ul,dface.l,dface.dl,fface.ul,fface.l,fface.dl = fface.ul,fface.l,fface.dl,uface.ul,uface.l,uface.dl,bface.dr,bface.r,bface.ur,dface.ul,dface.l,dface.dl

def fi():
    fface.counterclockwise()
    uface.dl,uface.d,uface.dr,lface.dr,lface.r,lface.ur,dface.ur,dface.u,dface.ul,rface.ul,rface.l,rface.dl = rface.ul,rface.l,rface.dl,uface.dl,uface.d,uface.dr,lface.dr,lface.r,lface.ur,dface.ur,dface.u,dface.ul

def di():
    dface.counterclockwise()
    fface.dl,fface.d,fface.dr,lface.dl,lface.d,lface.dr,bface.dl,bface.d,bface.dr,rface.dl,rface.d,rface.dr = rface.dl,rface.d,rface.dr,fface.dl,fface.d,fface.dr,lface.dl,lface.d,lface.dr,bface.dl,bface.d,bface.dr

def bi():
    bface.counterclockwise()
    uface.ur,uface.u,uface.ul,rface.dr,rface.r,rface.ur,dface.dl,dface.d,dface.dr,lface.ul,lface.l,lface.dl = lface.ul,lface.l,lface.dl,uface.ur,uface.u,uface.ul,rface.dr,rface.r,rface.ur,dface.dl,dface.d,dface.dr

def execute(moves):
    for move in moves.split():
        if move == 'U': u()
        if move == "U'": ui()
        if move == 'U2': 
            for i in range(2): u()
        if move == 'R': r()
        if move == "R'": ri()
        if move == 'R2': 
            for i in range(2): r()
        if move == 'L': l()
        if move == "L'": li()
        if move == 'L2': 
            for i in range(2): l()
        if move == 'F': f()
        if move == "F'": fi()
        if move == 'F2': 
            for i in range(2): f()
        if move == 'D': d()
        if move == "D'": di()
        if move == 'D2': 
            for i in range(2): d()
        if move == 'B': b()
        if move == "B'": bi()
        if move == 'B2': 
            for i in range(2): b()

def undo(prev_moves):
    for move in list(reversed(prev_moves.split())):
        if move == 'U': ui()
        if move == "U'": u()
        if move == 'U2': 
            for i in range(2): u()
        if move == 'R': ri()
        if move == "R'": r()
        if move == 'R2': 
            for i in range(2): r()
        if move == 'L': li()
        if move == "L'": l()
        if move == 'L2': 
            for i in range(2): l()
        if move == 'F': fi()
        if move == "F'": f()
        if move == 'F2': 
            for i in range(2): f()
        if move == 'D': di()
        if move == "D'": d()
        if move == 'D2': 
            for i in range(2): d()
        if move == 'B': bi()
        if move == "B'": b()
        if move == 'B2': 
            for i in range(2): b()

def cross_solved():
    return [dface.u,dface.l,dface.r,dface.d] == [white,white,white,white] and [fface.d,lface.d,rface.d,bface.d] == [blue,orange,red,green]

def render_exit():
    render()
    exit()

yellow = 0
orange = 1
blue = 2
red = 3
green = 4
white = 5
blank = 6

pixels = ['🟨','🟧','🟦','🟥','🟩','⬜️','  ']

uface = Face(yellow)
lface = Face(orange)
fface = Face(blue)
rface = Face(red)
bface = Face(green)
dface = Face(white)

blankface = Face(blank)

# scramble
scramble = "F' R2 D2 R'"
execute(scramble)
render()
print('scramble:',scramble)

# solve cross
# "U U' U2 R R' R2 L L' L2 F F' F2 D D' D2 B B' B2"
moves = "U U' U2 R R' R2 L L' L2 F F' F2 D D' D2 B B' B2".split()
for move1 in moves:
    execute(move1)
    if cross_solved():
        print('cross:',move1)
        render_exit()
    for move2 in moves:
        execute(move2)
        if cross_solved(): 
            print('cross:',move1,move2)
            render_exit()
        for move3 in moves:
            execute(move3)
            if cross_solved(): 
                print('cross:',move1,move2,move3)
                render_exit()
            for move4 in moves:
                execute(move4)
                if cross_solved(): 
                    print('cross:',move1,move2,move3,move4)
                    render_exit()
                    
                else: undo(move4)

            undo(move3)

        undo(move2)

    undo(move1)

render()

# render()
# undo('U2' + ' ' + 'F')
# render()
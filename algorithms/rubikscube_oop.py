import time
import random
import os

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

def cross_solvable(n):
    return [dface.u,dface.l,dface.r,dface.d].count(white) >= 4 - (8 - n)

def custom_scramble():
    os.system('clear')
    render()
    scramble = ''

    input_ = input().upper()
    while True:
        if input_ in moves:
            execute(input_)
            os.system('clear')
            render()

            scramble += input_ + ' '
            print('scramble:',scramble )
        elif input_ == '':
            break

        input_ = input().upper()

def random_scramble():
    os.system('clear')

    scramble_move_list = ["R"]
    for i in range(7):
        scramble_move_list.append(random.choice([x for x in real_moves if x[0] != scramble_move_list[-1][0]]))
    scramble = ' '.join(scramble_move_list)

    # scramble = "R F R2 L D2 F2 L F'"

    execute(scramble)
    render()
    print('scramble:',scramble)

def render_exit():
    render()
    runtime = time.time() - start
    print('runtime:', runtime)
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

real_moves = "U U' U2 R R' R2 L L' L2 F F' F2 D D' D2 B B' B2".split()
moves = "N U U' U2 R R' R2 L L' L2 F F' F2 D D' D2 B B' B2".split()

# custom_scramble()
random_scramble()

tperm = "R U R' U' R' F R2 U' R' U' R U R' F'"
uaperm = "F2 U L R' F2 L' R U F2"
ubperm = "F2 U' L R' F2 L' R U' F2"
def pll_solved():
    return [fface.ul,fface.u,fface.ur,lface.ul,lface.u,lface.ur,rface.ul,rface.u,rface.ur,bface.ul,bface.u,bface.ur] == [blue,blue,blue,orange,orange,orange,red,red,red,green,green,green]

def headlights_solved():
    return uface.ul == uface.ur and lface.ul == lface.ur and rface.ul == rface.ur and bface.ul == bface.ur

def pll():
    print('pll')
    for move1 in ["N",tperm]: # create headlights
        execute(move1)
        for move2 in ["N","U","U'","U2"]: # turn uface
            execute(move2)
            for move3 in ["N",tperm]: # create all headlights
                execute(move3)
                if headlights_solved():
                    for move4 in ["N","U","U'","U2"]: # turn uface
                        execute(move4)
                        for move5 in ["N",uaperm,ubperm]: # solve
                            execute(move5)
                            for move6 in ["N","U","U'","U2"]: # solve
                                execute(move6)
                                if pll_solved():
                                    print(move1,move2,move3)
                                    print(move4,move5)
                                    render()
                                    print('runtime:',time.time() - start)
                                    exit()
                                undo(move6)
                            undo(move5)
                        undo(move4)
                undo(move3)
            undo(move2)
        undo(move1)


def yellow_cross_solved():
    return [uface.u,uface.l,uface.r,uface.d] == [yellow,yellow,yellow,yellow]

def yellow_face_solved():
    return [uface.u,uface.l,uface.r,uface.d,uface.ul,uface.ur,uface.dl,uface.dr] == [yellow for _ in range(8)]

def oll_solve_cross():
    print('full yellow face')
    for move1 in ["N","U","U'","U2"]: 
        execute(move1)
        for alg1 in ["N","R U R' U R U2 R'","R U2 R' U' R U' R'","R2 D R' U2 R D' R' U2 R'","R' F R B' R' F' R B","R' F' L F R F' L' F","R U2 R' U' R U R' U' R U' R'","R U2 R2 U' R2 U' R2 U2 R"]:
            execute(alg1) # sune, antisune, superman, bow, fatboy, fastcross, slowcross
            if yellow_face_solved():
                print(move1,alg1)
                render()
                pll()
                exit()
            undo(alg1)
        undo(move1)

def oll_create_cross():
    # create cross
    print('creating yellow cross')
    for move1 in ["N","F R U R' U' F'"]: # solve dot
        execute(move1)
        for move2 in ["N","U","U'","U2"]: # turn uface
            execute(move2)
            for move3 in ["N","F U R U' R' F'","F R U R' U' F'"]: # solve L / bar
                execute(move3)
                if yellow_cross_solved():
                    print(move1,move2,move3)
                    render()
                    oll_solve_cross()
                undo(move3)
            undo(move2)
        undo(move1)



    

def winter_summer_positions():
    return [[fface.ur,uface.dr,uface.r,rface.ul,rface.u],[fface.ul,lface.ur,lface.u,uface.dl,uface.l],[fface.ur,uface.dr,lface.u,rface.ul,uface.l],[fface.ul,lface.ur,uface.r,uface.dl,rface.u]]

def f2lslot(i):
    return [[dface.ur,fface.dr,fface.r,rface.dl,rface.l],[dface.ul,lface.dr,lface.r,fface.dl,fface.l],[dface.dl,bface.dr,bface.r,lface.dl,lface.l],[dface.dr,rface.dr,rface.r,bface.dl,bface.l]][i]

f2lpair_colours = [[blue,red],[orange,blue],[green,orange],[red,green]]

def prev_f2lpairs_done(i):
    for x in range(i):
        col1,col2 = f2lpair_colours[i]
        if [white,col1,col1,col2,col2] != f2lslot(x):
            return False
    return True


def f2l(i):
    if i == 4: 
        # render()
        oll_create_cross()
        return()
    for move1 in moves:
        execute(move1)
        for move2 in moves:
            execute(move2)
            for move3 in moves:
                execute(move3)
                for move4 in moves:
                    execute(move4)
                    for move5 in ["N","U","U'","U2"]:
                        execute(move5)
                        col1,col2 = f2lpair_colours[i]
                        if [white,col1,col1,col2,col2] in winter_summer_positions():
                            if cross_solved(): # and prev_f2lpairs_done(i):
                                undo(move5)

                                # render()
                                # print(move1,move2,move3,move4)
                                
                                for move6 in moves:
                                    execute(move6)
                                    for move7 in moves:
                                        execute(move7)
                                        for move8 in moves:
                                            execute(move8)
                                            for move9 in moves:
                                                execute(move9)
                                                if [white,col1,col1,col2,col2] == f2lslot(i):
                                                    if cross_solved(): # and prev_f2lpairs_done(i):
                                                        for move in [move1,move2,move3,move4,move6,move7,move8,move9]:
                                                            print(move, end = ' ')
                                                        print()

                                                        render()
                                                        f2l(i+1)
                                                        exit()
                                                undo(move9)
                                            undo(move8)
                                        undo(move7)
                                    undo(move6)
                        undo(move5)
                    undo(move4)
                undo(move3)
            undo(move2)
        undo(move1)






# # ====================================================================================

# # cross

unsolvable_optimizations = 0
positions_analyzed = 0
start = time.time()

for move1 in moves:
    execute(move1)
    for move2 in moves:
        if move2[0] == move1[0] and move2 != 'N': continue
        execute(move2)
        for move3 in moves:
            if move3[0] == move2[0] and move3 != 'N': continue
            execute(move3)
            for move4 in moves:
                if move4[0] == move3[0] and move4 != 'N': continue
                execute(move4)
                for move5 in moves:
                    if move5[0] == move4[0] and move5 != 'N': continue
                    execute(move5)
                    if cross_solvable(5) != True:
                        undo(move5)
                        unsolvable_optimizations += 18 ** 3
                        continue
                    for move6 in moves:
                        if move6[0] == move5[0] and move6 != 'N': continue
                        execute(move6)
                        if cross_solvable(6) != True:
                            undo(move6)
                            unsolvable_optimizations += 18 ** 2
                            continue
                        for move7 in moves:
                            if move7[0] == move5[0] and move7 != 'N': continue
                            execute(move7)
                            if cross_solvable(7) != True:
                                undo(move7)
                                unsolvable_optimizations += 18 ** 1
                                continue
                            for move8 in moves:
                                if move8[0] == move7[0] and move8 != 'N': continue
                                execute(move8)
                                if cross_solved(): 
                                    print('cross: ',end = '')
                                    for move in (move1,move2,move3,move4,move5,move6,move7,move8):
                                        if move != 'N':
                                            print(move,end = ' ')
                                    print()


                                    print('unsolvable_optimizations:',unsolvable_optimizations)
                                    print('positions analyzed:', positions_analyzed)
                                    # render_exit()  
                                    render()
                                    f2l(0)
                                    exit()

                                positions_analyzed += 1

                                undo(move8)
                            undo(move7)
                        undo(move6)
                    undo(move5)
                undo(move4)
            undo(move3)
        undo(move2)
    undo(move1)

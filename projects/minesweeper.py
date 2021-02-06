#import os
import turtle
import random
#os.system('clear')
t=turtle.Turtle()
t.hideturtle()
t.pensize(5)
screen = turtle.Screen()
screen.setup(1200,900)
screen.tracer(0)
drawflag = False
side = 50
uncoveredsquares = 0
class Square:
    def __init__(self, x, y, fillcolor,number, state): #this function is called when creating a Square object
        self.x = x - 300
        self.y = y - 300
        self.fillcolor = fillcolor
        self.number = number
        self.state = state
    def draw(self): 
        t.penup()
        t.goto(self.x,self.y)
        t.pendown()
        t.color("black",self.fillcolor) 
        t.begin_fill()
        for _ in range(4):
            t.fd(side); t.lt(90)
        t.end_fill()    
        global uncoverflag
        if uncoverflag:
            global uncoveredsquares
            uncoveredsquares += 1
        print('uncoveredsquares from draw() = ',uncoveredsquares)
    def draw_num(self):
        t.pu()
        t.goto(self.x+20,self.y+15)
        t.pd()
        t.write(self.number, font=("Arial", 20, "bold"))
    @staticmethod
    def find(x,y): #static method - we 
        for square in li_objects:
            if square.x == x and square.y == y:
                return square
    
    def findUp(self):
        return self.find(self.x, self.y+side)
    def findDown(self):
        return self.find(self.x, self.y-side)  
    def findLeft(self):
        return self.find(self.x-side, self.y)
    def findRight(self):
        return self.find(self.x+side, self.y)
    def findTopLeft(self):
        return self.find(self.x-side, self.y+side)
    def findTopRight(self):
        return self.find(self.x+side, self.y+side)
    def findLowerLeft(self):
        return self.find(self.x-side, self.y-side)
    def findLowerRight(self):
        return self.find(self.x+side, self.y-side)

def static_draw(x,y,fillcolor):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("black",fillcolor) 
    t.begin_fill()
    for _ in range(4):
        t.fd(side); t.lt(90)
    t.end_fill()    

uncoverflag = False
safesquares = 100
d = {}
for x in range(10):
    for y in range(10):
        d[10*x+y] = Square(x*side,y*side,'medium sea green',9,'covered')
        d[10*x+y].draw()
        if random.randrange(4) == 0:
            d[10*x+y].fillcolor = 'dimgrey'
            d[10*x+y].number = 10
            safesquares -= 1

uncoverflag = True
        
li_objects = [d[key] for key in d] #objects '<__main__.Square object at 0x10c03f1c0>'
li_keys = [key for key in d] #keys '25'

uncoveredsquares = 0
print('uncoveredsquares = ', uncoveredsquares)

playflag = True

def mouseclick(x,y):
    if 250 < x < 350 and 10 < y < 50:
        set_game()
    try:
        global playflag
        global uncoveredsquares
        global safesquares
        if playflag:
            square = Square.find(x-x%50,y-y%50)
            if square.number == 10:
                for square in li_objects:
                    if square.number == 10:
                        square.draw()
                        #playflag = False
            elif square.number == 0:
                square.draw()
                clear(square) 
            else:
                Square.find(x-x%50,y-y%50).draw()
                Square.find(x-x%50,y-y%50).draw_num()
            screen.update()
            
    except:
        pass

screen.onclick(mouseclick,1)

usedsquares = []

    
def clear(x): #uses recursion to reveal white squares
    global usedsquares
    if x not in usedsquares:
        while True:
            if x not in usedsquares:
                try:
                    if x.findUp().fillcolor == 'white':
                        usedsquares.append(x)
                        x.findUp().draw()

                        clear(x.findUp())
                    else:
                        x.findUp().draw()
                        x.findUp().draw_num()
                except:
                    pass
            #if x not in usedsquares:
                try:
                    if x.findRight().fillcolor == 'white':
                        usedsquares.append(x)
                        x.findRight().draw()
                        clear(x.findRight())
                    else:
                        x.findRight().draw()
                        x.findRight().draw_num()
                except:
                    pass
            #if x not in usedsquares:
                try:
                    if x.findDown().fillcolor == 'white':
                        usedsquares.append(x)
                        x.findDown().draw()
                        clear(x.findDown())
                        
                    else:
                        x.findDown().draw()
                        x.findDown().draw_num()
                except:
                    pass
            #if x not in usedsquares:
                try:
                    if x.findLeft().fillcolor == 'white':
                        usedsquares.append(x)
                        x.findLeft().draw()
                        clear(x.findLeft())
                        
                    else:
                        x.findLeft().draw()
                        x.findLeft().draw_num()
                except:
                    pass
                try:
                    if x.findTopRight().fillcolor == 'white':
                        usedsquares.append(x)
                        x.findTopRight().draw()
                        clear(x.findTopRight())
                    else:
                        x.findTopRight().draw()
                        x.findTopRight().draw_num()
                except:
                    pass
                try:
                    if x.findTopLeft().fillcolor == 'white':
                        usedsquares.append(x)
                        x.findTopLeft().draw()
                        clear(x.findTopLeft())
                    else:
                        x.findTopLeft().draw()
                        x.findTopLeft().draw_num()
                except:
                    pass
                try:
                    if x.findLowerRight().fillcolor == 'white':
                        usedsquares.append(x)
                        x.findLowerRight().draw()
                        clear(x.findLowerRight())
                    else:
                        x.findLowerRight().draw()
                        x.findLowerRight().draw_num()
                except:
                    pass
                try:
                    if x.findLowerLeft().fillcolor == 'white':
                        usedsquares.append(x)
                        x.findLowerLeft().draw()
                        clear(x.findLowerLeft())
                    else:
                        x.findLowerLeft().draw()
                        x.findLowerLeft().draw_num()
                except:
                    pass
            else:
                usedsquares.append(x)
                break
            
flaggedsquares = []

def mouseclick2(x,y):

    if (x//50*50,y//50*50) not in flaggedsquares: #hasn't been flagged
        static_draw(x//50*50,y//50*50,'orange')
        flaggedsquares.append((x//50*50,y//50*50))
    else:
        static_draw(x//50*50,y//50*50,'medium sea green') #remove flag
        flaggedsquares.remove((x//50*50,y//50*50))
    screen.update()

screen.onclick(mouseclick2,2)

def write2(x,y,text,fontsize=15,style = 'normal',pencolor = 'black'):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.pencolor(pencolor)
    t.write(text,font=("arial", fontsize, style))


def instructions():
    colours = ('white','lightblue','green','red','purple','purple','dimgrey','orange')
    nums = ['',1,2,3,4,'x','','']
    demotiles = {}
    global uncoverflag
    uncoverflag = False
    for x in range(8):
        demotiles[x] = Square(-250,520-(80*x),colours[x],nums[x],'uncovered')
        demotiles[x].draw()
        demotiles[x].draw_num()
    uncoverflag = True
    instructioncount = 0
    y = 280

    texts = ('Click on tiles to reveal them',[f'{x} bombs surrounding tile' for x in range(5)],'x bombs surrounding tile (5,6,7,8)','Bomb','Flagged as bomb (right click)')
    for text in texts:
        if type(text) == list:
            for iteration in text:
                write2(-550,y,iteration,15,'bold')
                y = y - 80
                instructioncount +=1
        elif type(text ) == str:
            write2(-550,y,text,15,'bold')
            y = y - 80
            instructioncount +=1

uncoveredsquares = 0
print('reset uncoveredsquares after instructions demotiles= ', uncoveredsquares)

def drawrectangle(x,y,text,colour,length=100,height=40,size=40):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("black",colour) 
    t.begin_fill()
    for _ in range(2):
        t.fd(length); t.lt(90)
        t.fd(height); t.lt(90)
    t.end_fill()    
    t.pu()
    t.goto(x+15,y+15)
    t.pd()
    t.write(text, font=("Arial", 20, "bold"))

usedsquares = []

def set_game():
    global usedsquares
    global d
    global playflag
    global safesquares

    playflag = True
    for square in li_objects:
        if square.number == 10:
            pass
        else:
            bombcount = 0
            try:
                if square.findUp().number == 10:
                    bombcount += 1
            except:
                pass
            try:
                if square.findRight().number == 10:
                    bombcount += 1
            except:
                pass
            try:
                if square.findDown().number == 10:
                    bombcount += 1
            except:
                pass
            try:
                if square.findLeft().number == 10:
                    bombcount += 1
            except:
                pass
            try:
                if square.findTopLeft().number == 10:
                    bombcount += 1
            except:
                pass
            try:
                if square.findTopRight().number == 10:
                    bombcount += 1
            except:
                pass
            try:
                if square.findLowerLeft().number == 10:
                    bombcount += 1
            except:
                pass
            try:
                if square.findLowerRight().number == 10:
                    bombcount += 1
            except:
                pass

            if bombcount == 0:
                square.fillcolor = 'white'
                square.number = 0
            elif bombcount == 1:
                square.fillcolor = 'lightblue'
                square.number = 1
            elif bombcount == 2:
                square.fillcolor = 'green'
                square.number = 2
            elif bombcount == 3:
                square.fillcolor = 'red'
                square.number = 3
            else:
                square.fillcolor = 'purple'
                square.number = bombcount

    write2(240,215,"These don't work (beta)",20,'normal')
    drawrectangle(250,160,'easy','lightgreen')
    drawrectangle(250,110,'medium','yellow')
    drawrectangle(250,60,'hard','orangered')
    drawrectangle(250,10,'reset','lightblue')

    write2(-300,240,'Minesweeper',80,'bold')
    write2(-50,215,'by Gordon Liang',30,'normal')
    instructions()

set_game()

print('total safe squares = ', safesquares)

screen.listen()
screen.update()
screen.mainloop()
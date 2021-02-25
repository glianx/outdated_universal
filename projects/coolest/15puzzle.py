#!/usr/bin/env python3
import turtle
import time
import threading
import random
import string
t=turtle.Turtle()
t.hideturtle()
t.pensize(5)
screen = turtle.Screen()
screen.setup(900,900)
t.speed(0)
screen.tracer(0,0)
screen.delay(0)
side = 100
counter = 0

screen.title("15 Puzzle")

colours1 = ["dodgerblue4", "dodgerblue2","turquoise","cyan"]
colour1,colour2,colour3,colour4 = [y for y in colours1]

colours2 = ["forestgreen","limegreen","mediumseagreen","aquamarine"]
colour5,colour6,colour7,colour8 = [x for x in colours2]

drawflag = True

class Square:

    def __init__(self, x, y, fillcolor,number):
        self.x = x
        self.y = y
        self.fillcolor = fillcolor
        self.number = number
    
    def draw(self):
        goto(self.x,self.y)
        t.color("black",self.fillcolor) 
        t.begin_fill()
        for _ in range(4):
            t.fd(side); t.lt(90)
        t.end_fill()    
        goto(self.x+30,self.y+30)
        t.write(self.number, font=("Arial", 40, "bold"))
   
    def find(self,x,y):
        for tile in (s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s0):
            if tile.x == x and tile.y == y:
                return tile
        
    def findUp(self):
        return self.find(self.x, self.y+side)
    def findDown(self):
        return self.find(self.x, self.y-side)  
    def findLeft(self):
        return self.find(self.x-side, self.y)
    def findRight(self):
        return self.find(self.x+side, self.y)
    
    def moveUp(self):
        self.y = self.y+side  
        if drawflag:
            self.draw()    
    def moveDown(self):
        self.y = self.y-side  
        if drawflag:
            self.draw()  
    def moveLeft(self):
        self.x = self.x-side
        if drawflag:
            self.draw()   
    def moveRight(self):
        self.x = self.x+side  
        if drawflag:
            self.draw()  
        
    def goUp(self):
        self.findUp().moveDown()
        self.moveUp()
        count()
    def goDown(self):
        self.findDown().moveUp()
        self.moveDown()
        count()
    def goLeft(self):
        self.findLeft().moveRight()
        self.moveLeft()
        count()
    def goRight(self):
        self.findRight().moveLeft()
        self.moveRight()
        count()



s1 = Square(-2*side,side,colour1,"1")
s2 = Square(-side,side,colour1,"2")
s3 = Square(0,side,colour1,"3")
s4 = Square(side,side,colour1,"4")
s5 = Square(-2*side,0,colour2,"5")
s6 = Square(-side,0,colour2,"6")
s7 = Square(0,0,colour2,"7")
s8 = Square(side,0,colour2,"8")
s9 = Square(-2*side,-side,colour3,"9")
s10 = Square(-side,-side,colour3,"10")
s11 = Square(0,-side,colour3,"11")
s12 = Square(side,-side,colour3,"12")
s13 = Square(-2*side,-2*side,colour4,"13")
s14 = Square(-side,-2*side,colour4,"14")
s15 = Square(0,-2*side,colour4,"15")

s0 = Square(side,-2*side,"white","")

def goto(x,y):
    t.pu()
    t.goto(x,y)
    t.pd()

def draw4x4():
    for x in (s1, s2, s3, s4, s5, s6, s7, s8, s9, 
        s10, s11, s12, s13, s14, s15, s0):
        x.draw()

    
draw4x4()


screen.onkey(s0.goDown,"Up")
screen.onkey(s0.goRight,"Left")
screen.onkey(s0.goUp,"Down")
screen.onkey(s0.goLeft,"Right")



def mouseclick(x,y):
    #print(x,y)
    #fix error here - timerthread starts twice
    global timerThread
    if not timerThread.is_alive():
        timerThread.start()
    if s0.x < x < s0.x+side and s0.y+side < y < s0.y+2*side:
        s0.goUp()
    elif s0.x < x < s0.x+side and s0.y-side < y < s0.y:
        s0.goDown()
    elif s0.x+side < x < s0.x+2*side and s0.y < y < s0.y+side:
        s0.goRight()
    elif s0.x-side < x < s0.x and s0.y < y < s0.y+side:
        s0.goLeft()
    
        #timerThread.start()
    #print(x,y)


timeflag = 1

screen.onscreenclick(mouseclick,1)

def timer():
    global start_time
    global end_time
    global timeflag
    start_time = time.time()
    global runningtime
    while True:
        time.sleep(1)
        end_time = time.time()
        runningtime = round(end_time - start_time)
        if timeflag == 0:
            break
        drawrectangle(-2*side+300,2*side+20,runningtime)



def popup():
    if counter>20:
        if s1.x == -2*side and s1.y == side and s1.findRight() == s2 and s2.findRight() == s3 and s3.findRight() == s4:
            if s1.findDown() == s5 and s2.findDown() == s6 and s3.findDown()==s7 and s4.findDown()==s8:
                if s5.findDown()==s9 and s6.findDown()==s10 and s7.findDown()==s11 and s8.findDown()==s12:
                    if s9.findDown()==s13 and s10.findDown()==s14 and s11.findDown()==s15:
                        global timeflag
                        timeflag = 0
                        global runningtime
                        s0.fillcolor = "cyan"
                        s0.draw()
                        if runningtime < 60:
                            message, textcolor = 'Congratulations! ✓','lightseagreen'
                        elif runningtime < 120:
                            message, textcolor = 'Excellent! ✓','mediumspringgreen'
                        elif runningtime < 180:
                            message, textcolor = 'Try harder','gold'
                        else:
                            message, textcolor = 'You\'re slow','red'
                        write(-2*side,-2*side-65,message,40, color = textcolor)
                        write(-200,-300,'Time: {}'.format(runningtime),30, color = textcolor)
                        write(0,-300,f'Moves: {counter}',30, color = textcolor)


def count():
    global counter
    counter = counter + 1
    if drawflag:
        drawrectangle(-2*side+110,2*side+20,counter)
    popup()
    
    
def drawrectangle(x,y,text,length = 80,height = 30):

    goto(x,y)
    t.color("white","white") 
    t.begin_fill()
    t.fd(length); t.lt(90)
    t.fd(height); t.lt(90)
    t.fd(length); t.lt(90)
    t.fd(height); t.lt(90)
    t.end_fill()  
    t.pencolor("black")
    t.write(text, font=("Arial", 30, "bold"))



def changecolour():

    global colour1, colour2, colour3, colour4, colour5, colour6, colour7, colour8
    global s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15
    colourgroup1 = (colour1, colour2, colour3, colour4)
    colour1, colour2, colour3, colour4,colour5, colour6, colour7, colour8 = colour5, colour6, colour7, colour8,colour1, colour2, colour3, colour4
    tiles = ((s1,s2,s3,s4),(s5,s6,s7,s8),(s9,s10,s11,s12),(s13,s14,s15))
    for group, colour in zip(tiles,colourgroup1):
        for x in group:
            x.fillcolor = colour
    draw4x4()



    
screen.onkey(changecolour, "c")


        
        
def write(x,y,text,size = 30, color = 'black'):

    goto(x,y)
    t.pencolor(color)
    t.write(text, font=("Arial", size, "bold"))

write(-2*side+220,2*side+20,"time: 0")
write(-2*side,2*side+20,"moves: 0")

y = 190
texts = ("↑ up","→ right","↓ down","← left","mouseclick = ↑↓←→","space = scramble","0 = reset count","c = colorchange","i = prank", "random = resetprank")
for text in texts:
    write(220,y,text,15)
    y = y - 30


timerThread = threading.Thread(target=timer)


def scramble_1():
    move = random.randint(0,3)
    if move == 0: 
        if s0.y != -2*side:
            s0.goDown()
    elif move == 1:
        if s0.x != side:
            s0.goRight()
    elif move == 2: 
        if s0.y != side:
            s0.goUp()
    elif move == 3:
        if s0.x != -2*side:
            s0.goLeft()
    

def scramble():
    global drawflag
    drawflag = False
    for _ in range(400):
        scramble_1()
    draw4x4()
    global counter 
    counter=0
    drawflag = True

def reset():
    global counter
    counter=0
    drawrectangle(-2*side+110,2*side+20,counter)
    global start_time
    start_time = time.time()

screen.onkey(reset,"0")
prankflag = True

def setprank():
    global prankflag
    if prankflag:
        s14.x,s14.y,s15.x,s15.y=s15.x,s15.y,s14.x,s14.y
        s14.draw()
        s15.draw()
        prankflag = False
    

screen.onkey(setprank,"i")

randomletter = random.choice(string.ascii_letters)

def resetprank():
    global prankflag
    if prankflag == False:
        s14.x,s14.y,s15.x,s15.y=s15.x,s15.y,s14.x,s14.y
        s14.draw()
        s15.draw()
        prankflag = True

screen.onkey(resetprank,randomletter)


                 
                        

screen.onkey(scramble,"space")
#draw title - 15 puzzle
write(-2*side,2*side+50,"15 Puzzle",60, "steel blue")


screen.listen()
screen.update()
screen.mainloop()

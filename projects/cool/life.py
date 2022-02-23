#conway's game of life
#you can find more information here: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
#to play, click some squares to set them as alive
#when you are happy with your setup, press space to start the simulation
#watch as the population grows and see if it can survive
import os
import turtle
import random
import time 
os.system('clear')
t=turtle.Turtle()
t.hideturtle()
t.pensize(5)
screen = turtle.Screen()
screen.setup(900,900)
screen.tracer(0)
drawflag = False
side = 30
class Square:
    def __init__(self, x, y, fillcolor):
        self.x = x - 300
        self.y = y - 300
        self.fillcolor = fillcolor

    def draw(self):
        t.penup()
        t.goto(self.x,self.y)
        t.pendown()
        t.color("black",self.fillcolor) 
        t.begin_fill()
        for _ in range(4):
            t.fd(side); t.lt(90)
        t.end_fill()    
    @staticmethod
    def find(x,y):
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
 
d = {}
for x in range(20):
    for y in range(20):
        d[f'{x}{y}'] = Square(x*side,y*side,'dimgray')
        d[f'{x}{y}'].draw()
        
li_objects = [d[key] for key in d] #objects '<__main__.Square object at 0x10c03f1c0>'
li_keys = [key for key in d] #keys '25'


def mouseclick(x,y):
    #square = Square.find(x-x%50,y-y%50)
    if Square.find(x-x%side,y-y%side).fillcolor == 'dimgray':
        Square.find(x-x%side,y-y%side).fillcolor = 'white'
        Square.find(x-x%side,y-y%side).draw()

    elif Square.find(x-x%side,y-y%side).fillcolor == 'white':
        Square.find(x-x%side,y-y%side).fillcolor = 'dimgray'
        Square.find(x-x%side,y-y%side).draw()

    screen.update()

screen.onclick(mouseclick,1)

def step():
    killedsquares = []
    bornsquares = []
    for square in li_objects:
        livecount = 0
        try:
            if square.findUp().fillcolor == 'white':
                livecount += 1
        except:
            pass
        try:
            if square.findDown().fillcolor == 'white':
                livecount += 1
        except:
            pass
        try:
            if square.findLeft().fillcolor == 'white':
                livecount += 1
        except:
            pass
        try:
            if square.findRight().fillcolor == 'white':
                livecount += 1
        except:
            pass
        try:
            if square.findTopLeft().fillcolor == 'white':
                livecount += 1
        except:
            pass
        try:
            if square.findTopRight().fillcolor == 'white':
                livecount += 1
        except:
            pass
        try:
            if square.findLowerLeft().fillcolor == 'white':
                livecount += 1
        except:
            pass
        try:
            if square.findLowerRight().fillcolor == 'white':
                livecount += 1
        except:
            pass
        #print(livecount)
        if square.fillcolor == 'white':
            if livecount != 2 and livecount != 3:
                killedsquares.append(square)
                #square.fillcolor = 'dimgray'
        if square.fillcolor == 'dimgray':
            if livecount == 3:
                bornsquares.append(square)
                #square.fillcolor = 'white'
                
    
    for square in killedsquares:
        square.fillcolor = 'dimgray'
        square.draw()
    for square in bornsquares:
        square.fillcolor = 'white'
        square.draw()
    screen.update()
screen.onkey(step, "s")

stopflag = False


def run():
   
    global stopflag
    
    while True:
        #time.sleep(0.1)
        step()
        
        total_live = 0
        
        for square in li_objects:
            if square.fillcolor == 'white':
                total_live += 1
        if total_live == 0:
            break
        
        if stopflag:
            break
        #if stopflag == False:
            #stopflag = True

    #elif stopflag == True:
        #stopflag = False
    
screen.onkey(run, "space")

def stop():
    pass
screen.onkey(stop, "0")

screen.listen()
screen.update()
screen.mainloop()
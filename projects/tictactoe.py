
import turtle
#import os
import random
import time 
#os.system('clear') 
t=turtle.Turtle()
t.hideturtle()
t.pensize(5)
screen = turtle.Screen()
screen.setup(800,800)
screen.tracer(0)
side = 150

xshift = -150
yshift = -150

xbuffer = 45
ybuffer = 30

class Square:
    def __init__(self,x,y,symbol):
        self.x = x + xshift
        self.y = y + yshift
        self.symbol = symbol
    def draw(self):
        t.penup()
        t.goto(self.x,self.y)
        t.pendown()
        t.color("black","lightblue") 
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
for x in range(3):
    for y in range(3):
        d[f'{x}{y}'] = Square(x*side,y*side,f'{x}{y}') #each one has unique symbol
        d[f'{x}{y}'].draw()
        #print(d[f'{x}{y}'].x,d[f'{x}{y}'].y)
    
li_objects = [d[key] for key in d] #objects '<__main__.Square object at 0x10c03f1c0>'
li_keys = [key for key in d] #keys '25'


def goto(x,y): #goto w/o drawing

    t.penup()
    t.goto(x,y)
    t.pendown()

usedsquares = []

playflag = True

def mouseclick(x,y):
    global playflag
    try:
        square = Square.find(x-x%side,y-y%side)
        
        if square not in usedsquares and playflag:
            if len(usedsquares) % 2 == 0: #even num of squares in usedsquares
                square.symbol = 'X'
            elif len(usedsquares) % 2 == 1: #odd num of squares in usedsquares
                square.symbol = 'O'

            goto(x-x%side + xbuffer,y-y%side + ybuffer)
            t.write(square.symbol, font=("Arial", 80, "bold"))
            usedsquares.append(square)
            
            for square in li_objects:
                try:
                    if square.findUp().symbol == square.symbol == square.findDown().symbol:
                        goto(-150,-200)
                        t.write(f'{square.symbol} wins!', font=("Arial", 40, "bold"))
                        playflag = False
                except:
                    pass
                try:
                    if square.findLeft().symbol == square.symbol == square.findRight().symbol:
                        goto(-150,-200)
                        t.write(f'{square.symbol} wins!', font=("Arial", 40, "bold"))
                        playflag = False
                except:
                    pass
                try:
                    if square.findTopLeft().symbol == square.symbol == square.findLowerRight().symbol:
                        goto(-150,-200)
                        t.write(f'{square.symbol} wins!', font=("Arial", 40, "bold"))
                        playflag = False
                except:
                    pass
                try:
                    if square.findTopRight().symbol == square.symbol == square.findLowerLeft().symbol:
                        goto(-150,-200)
                        t.write(f'{square.symbol} wins!', font=("Arial", 40, "bold"))
                        playflag = False
                except:
                    pass
            if len(usedsquares) == 9 and playflag:
                goto(-150,-200)
                t.write('Tie', font=("Arial", 40, "bold"))
    except:
        pass

screen.onclick(mouseclick,1)

screen.listen()
screen.update()
screen.mainloop()

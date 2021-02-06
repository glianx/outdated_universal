#!/usr/bin/env python3
import turtle
import random
import time
import threading
t=turtle.Turtle()
t.hideturtle()

s = 50
t.pensize(5)
x,y=-390,-200
showmovesflag=0

m=0
m2=0
screen = turtle.Screen()
screen.setup(1200,900)
t.speed(0)
screen.tracer(0,0)
screen.delay(0)
green='MediumSeaGreen'
red='orange red'
blue='royal blue'
orange='dark orange'
yellow='gold'
white='white smoke'
screen.bgcolor("white")

def drawSquare(x, y, color):

    t.color("black", color) 
    t.pu()
    t.setpos(x, y)
    t.pd()
    t.begin_fill()
    for x in range(4):
        t.fd(s); t.lt(90)
    t.end_fill()  

def drawSide(x, y, colors):

    drawSquare(x, y,  colors[0])
    drawSquare(x+s, y, colors[1])
    drawSquare(x+2*s, y, colors[2])

    t.goto(x+2*s,y+s)
    
    drawSquare(x, y+s, colors[3])
    drawSquare(x+s, y+s, colors[4])
    drawSquare(x+2*s, y+s, colors[5])

    t.goto(x+2*s,y+2*s)
    
    drawSquare(x, y+2*s, colors[6])
    drawSquare(x+s, y+2*s, colors[7])
    drawSquare(x+2*s, y+2*s, colors[8])
def drawCube():
    #t.clear()
    countmoves()
    drawSide(0-2*s, 0,    [dlF, dF, drF, lF, F, rF, ulF, uF, urF]) #frontside
    drawSide(-3*s-2*s, 0, [dLb, dL, dLf, Lb, L, Lf, uLb, uL, uLf]) #leftside
    drawSide(3*s-2*s, 0,  [dRf, dR, dRb, Rf, R, Rb, uRf, uR, uRb]) #rightside
    drawSide(6*s-2*s, 0,  [drB, dB, dlB, rB, B, lB, urB, uB, ulB]) #backside
    drawSide(0-2*s, 3*s,  [Ulf, Uf, Urf, Ul, U, Ur, Ulb, Ub, Urb]) #upside
    drawSide(0-2*s, -3*s, [Dlb, Db, Drb, Dl, D, Dr, Dlf, Df, Drf]) #downside
    if showmovesflag==0:
        showmoves(250,250,m)
        
    else:
        showmoves(250,175,m)
        
    screen.update()



def write():
    
    global x
    global y
    x=x+30
    
    if x>330:
        x=-360
        y=y-25
        
    t.pu()
    t.goto(x,y)
    t.pencolor("grey")
    t.pd()
def undo():

    t.undo()

screen.onkey(undo,"z") 

def u():
    
    global ulF, uF, urF, uRf, uR, uRb, urB, uB, ulB, uLb, uL, uLf
    ulF, uF, urF, uRf, uR, uRb, urB, uB, ulB, uLb, uL, uLf =uRf, uR, uRb, urB, uB, ulB, uLb, uL, uLf, ulF, uF, urF
    global Ulf, Urf, Urb, Ulb, Uf, Ur, Ub, Ul
    Ulf, Urf, Urb, Ulb, Uf, Ur, Ub, Ul= Urf, Urb, Ulb, Ulf, Ur, Ub, Ul, Uf

    drawCube()
    write()
    t.write("U", font=("Arial", 20, "normal"))
    
screen.onkey(u,"u")

def ui():

    global ulF, uF, urF, uRf, uR, uRb, urB, uB, ulB, uLb, uL, uLf
    ulF, uF, urF, uRf, uR, uRb, urB, uB, ulB, uLb, uL, uLf = uLb, uL, uLf, ulF, uF, urF, uRf, uR, uRb, urB, uB, ulB,
    global Ulf, Urf, Urb, Ulb, Uf, Ur, Ub, Ul
    Ulf, Urf, Urb, Ulb, Uf, Ur, Ub, Ul=Ulb,Ulf, Urf,Urb, Ul,Uf, Ur, Ub,
    drawCube()
    write()
    t.write("U'", font=("Arial", 20, "normal"))
    
screen.onkey(ui,"U")

def r():

    global urF, rF, drF, Drf, Dr, Drb, drB, rB, urB, Urb, Ur, Urf
    urF, rF, drF, Drf, Dr, Drb, drB, rB, urB, Urb, Ur, Urf=Drf, Dr, Drb, drB, rB, urB, Urb, Ur, Urf,  urF, rF, drF
    global dRf,dRb,uRb,uRf, dR,Rb,uR,Rf
    dRf,dRb,uRb,uRf,dR,Rb,uR,Rf=dRb,uRb,uRf,dRf,Rb,uR,Rf,dR
    drawCube()
    write()
    t.write("R", font=("Arial", 20, "normal"))
    
screen.onkey(r,"r")

def ri():

    global urF, rF, drF, Drf, Dr, Drb, drB, rB, urB, Urb, Ur, Urf
    urF, rF, drF, Drf, Dr, Drb, drB, rB, urB, Urb, Ur, Urf=Urb, Ur, Urf,urF, rF, drF, Drf, Dr, Drb, drB, rB, urB,
    global dRf,dRb,uRb,uRf, dR,Rb,uR,Rf
    dRf,dRb,uRb,uRf,dR,Rb,uR,Rf=uRf,dRf,dRb,uRb,Rf,dR,Rb,uR
    drawCube()
    write()
    t.write("R'", font=("Arial", 20, "normal"))

screen.onkey(ri,"R")

def f():

    global Ulf, Uf, Urf,dLf, Lf, uLf, Drf, Df, Dlf, uRf, Rf, dRf
    Ulf, Uf, Urf,dLf, Lf, uLf, Drf, Df, Dlf, uRf, Rf, dRf=dLf, Lf, uLf, Drf, Df, Dlf, uRf, Rf, dRf,Ulf, Uf, Urf,
    global dlF,drF,urF,ulF,lF,dF,rF,uF
    dlF,drF,urF,ulF,lF,dF,rF,uF=drF,urF,ulF,dlF,dF,rF,uF,lF
    drawCube()
    write()
    t.write("F", font=("Arial", 20, "normal"))

screen.onkey(f,"f",)

def fi():

    global Ulf, Uf, Urf,dLf, Lf, uLf, Drf, Df, Dlf, uRf, Rf, dRf
    Ulf, Uf, Urf,dLf, Lf, uLf, Drf, Df, Dlf, uRf, Rf, dRf=uRf, Rf, dRf,Ulf, Uf, Urf,dLf, Lf, uLf, Drf, Df, Dlf
    global dlF,drF,urF,ulF,lF,dF,rF,uF
    dlF,drF,urF,ulF,lF,dF,rF,uF=ulF,dlF,drF,urF,uF,lF,dF,rF
    drawCube()
    write()
    t.write("F'", font=("Arial", 20, "normal"))

screen.onkey(fi,"F")

def l():

    global  Ulb, Ul, Ulf, dlB,lB, ulB,Dlf, Dl, Dlb,ulF, lF, dlF
    Ulb, Ul, Ulf, dlB,lB, ulB,Dlf, Dl, Dlb,ulF, lF, dlF=dlB,lB, ulB,Dlf, Dl, Dlb,ulF, lF, dlF,Ulb, Ul, Ulf
    global dLb,dLf,uLf,uLb,dL,Lf,uL,Lb
    dLb,dLf,uLf,uLb,dL,Lf,uL,Lb=dLf,uLf,uLb,dLb,Lf,uL,Lb,dL
    drawCube()
    write()
    t.write("L", font=("Arial", 20, "normal"))


screen.onkeyrelease(l,"l")

def li():

    global  Ulb, Ul, Ulf, dlB,lB, ulB,Dlf, Dl, Dlb,ulF, lF, dlF
    Ulb, Ul, Ulf, dlB,lB, ulB,Dlf, Dl, Dlb,ulF, lF, dlF=ulF, lF, dlF,Ulb, Ul, Ulf, dlB,lB, ulB,Dlf, Dl, Dlb
    global dLb,dLf,uLf,uLb,dL,Lf,uL,Lb
    dLb,dLf,uLf,uLb,dL,Lf,uL,Lb=uLb,dLb,dLf,uLf,Lb,dL,Lf,uL
    drawCube()
    write()
    t.write("L'", font=("Arial", 20, "normal"))

screen.onkey(li,"L")

def d():

    global dlF, dF, drF, dLb, dL, dLf, drB, dB, dlB, dRf, dR, dRb
    dlF, dF, drF, dLb, dL, dLf, drB, dB, dlB, dRf, dR, dRb=dLb, dL, dLf, drB, dB, dlB, dRf, dR, dRb,dlF, dF, drF
    global Drf, Dlf, Dlb, Drb, Df, Dl, Db, Dr
    Drf, Dlf, Dlb, Drb, Df, Dl, Db, Dr = Dlf, Dlb, Drb,Drf,Dl, Db, Dr, Df
    drawCube()
    write()
    t.write("D", font=("Arial", 20, "normal"))

screen.onkey(d,"d")

def di():

    global dlF, dF, drF, dLb, dL, dLf, drB, dB, dlB, dRf, dR, dRb
    dlF, dF, drF, dLb, dL, dLf, drB, dB, dlB, dRf, dR, dRb=dRf, dR, dRb,dlF, dF, drF, dLb, dL, dLf, drB, dB, dlB
    global Drf, Dlf, Dlb, Drb, Df, Dl, Db, Dr
    Drf, Dlf, Dlb, Drb, Df, Dl, Db, Dr = Drb,Drf, Dlf, Dlb,Dr,Df, Dl, Db
    drawCube()
    write()
    t.write("D'", font=("Arial", 20, "normal"))

screen.onkey(di,"D")

def b():

    global Ulb, Ub, Urb, uRb, Rb, dRb, Drb, Db, Dlb, dLb, Lb, uLb
    Ulb, Ub, Urb, uRb, Rb, dRb, Drb, Db, Dlb, dLb, Lb, uLb=uRb, Rb, dRb, Drb, Db, Dlb, dLb, Lb, uLb,Ulb, Ub, Urb
    global ulB, urB, drB, dlB, uB, rB, dB, lB
    ulB, urB, drB, dlB, uB, rB, dB, lB=urB, drB, dlB,ulB,rB, dB, lB,uB
    drawCube()
    write()
    t.write("B", font=("Arial", 20, "normal"))

screen.onkey(b,"b")

def bi():

    global Ulb, Ub, Urb, uRb, Rb, dRb, Drb, Db, Dlb, dLb, Lb, uLb
    Ulb, Ub, Urb, uRb, Rb, dRb, Drb, Db, Dlb, dLb, Lb, uLb=dLb, Lb, uLb, Ulb, Ub, Urb, uRb, Rb, dRb, Drb, Db, Dlb
    global ulB, urB, drB, dlB, uB, rB, dB, lB
    ulB, urB, drB, dlB, uB, rB, dB, lB=dlB,ulB, urB, drB,lB,uB, rB, dB
    drawCube()
    write()
    t.write("B'", font=("Arial", 20, "normal"))

screen.onkey(bi,"B") 



def r2():

    r()
    r()
def u2():

    u()
    u()
def f2():

    f()
    f()
def l2():

    l()
    l()
def d2():

    d()
    d()
def b2():

    b()
    b()


def sexymove():

    r()
    u()
    ri()
    ui()
def sexymove2():

    li()
    ui()
    l()
    u()
def sledgehammer():

    ri()
    f()
    r()
    fi()
def sledgehammer2():

    l()
    fi()
    li()
    f()
def reversesexy():
    u()
    r()
    ui()
    ri()    
def reversesexy2():
    ui()
    li()
    u()
    l()


def cross_u1(): #u layer, white oriented
    
    if Uf==white:
        if uF==blue:
            f2()
    if Uf==white:
        if uF==red:
            ui()
            r2()
    if Uf==white:
        if uF==orange:
            u()
            l2()
    if Uf==white:
        if uF==green:
            u2()
            b2()
    if Uf==white:
        if uF==blue:
            f2()

    if Ul==white:
        if uL==blue:
            ui()
            f2()
    if Ul==white:
        if uL==orange:
            l2()
    if Ul==white:
        if uL==green:
            u()
            b2()
    if Ul==white:
        if uL==red:
            u2()
            r2()

    if Ur==white:
        if uR==red:
            r2()
    if Ur==white:
        if uR==blue:
            u()
            f2()
    if Ur==white:
        if uR==green:
            ui()
            b2()
    if Ur==white:
        if uR==orange:
            u2()
            l2()
    if Ub==white:
        if uB==green:
            b2()
    if Ub==white:
        if uB==red:
            u()
            r2()
    if Ub==white:
        if uB==orange:
            ui()
            l2()
    if Ub==white:
        if uB==blue:
            u2()
            f2()
    
    
def cross_u2(): #u layer, white flipped
    
    if uF==white:
        if Uf==blue:
            u()
            l()
            fi()
            li()
    if uF==white:
        if Uf==orange:
            fi()
            l()
            f()
    if uF==white:
        if Uf==red:
            f()
            ri()
            fi()

    if uF==white:
        if Uf==green:
            ui()
            r()
            bi()
            ri()

    if uR==white:
        if Ur==blue:
            ri()
            f()
            r()
    if uR==white:
        if Ur==green:
            r()
            bi()
            ri()
    if uR==white:
        if Ur==red:
            u()
            f()
            ri()
            fi()
        
    if uR==white:
        if Ur==orange:
            u()
            fi()
            l()
            f()

    if uL==white:
        if Ul==blue:
            l()
            fi()
            li()
    if uL==white:
        if Ul==green:
            li()
            b()
            l()

    if uL==white:
        if Ul==orange:
            ui()
            fi()
            l()
            f()
    if uL==white:
        if Ul==red:
            u()
            b()
            r()
            bi()

    if uB==white:
        if Ub==red:
            bi()
            r()
            b()
    if uB==white:
        if Ub==orange:
            b()
            li()
            bi()
    if uB==white:
        if Ub==green:
            u()
            r()
            bi()
            ri()
    if uB==white:
        if Ub==blue:
            u()
            ri()
            f()
            r()


def cross_e1(): #e layer, front
    
    if lF==white:
        if Lf==orange:
            l()
    if lF==white:
        if Lf==red:
            d2()
            l()
            d2()
    if lF==white:
        if Lf==blue:
            di()
            l()
            d()
    if lF==white:
        if Lf==green:
            d()
            l()
            di()

    if rF==white:
        if Rf==red:
            ri()
    if rF==white:
        if Rf==orange:
            d2()
            ri()
            d2()

    if rF==white:
        if Rf==blue:
            d()
            ri()
            di()
    if rF==white:
        if Rf==green:
            di()
            ri()
            d()

    if Lf==white:
        if lF==blue:
            fi()
    if Lf==white:
        if lF==orange:
            d()
            fi()
            di()
    if Lf==white:
        if lF==red:
            di()
            fi()
            d()

    if Lf==white:
        if lF==green:
            d2()
            fi()
            d2()
    
    if Rf==white:
        if rF==blue:
            f()
    if Rf==white:
        if rF==orange:
            d()
            f()
            di()
            
    if Rf==white:
        if rF==red:
            di()
            f()
            d()

    if Rf==white:
        if rF==green:
            d2()
            f()
            d2()

def cross_e2(): # e layer, back
    
    if lB==white:
        if Lb==orange:
            li()
    if lB==white:
        if Lb==blue:
            di()
            li()
            d()

    if lB==white:
        if Lb==green:
            d()
            li()
            di()

    if lB==white:
        if Lb==red:
            d2()
            li()
            d2()
     
    if rB==white:
        if Rb==red:
            r()
    if rB==white:
        if Rb==blue:
            d()
            r()
            di()
    if rB==white:
        if Rb==green:
            di()
            r()
            d()
    if rB==white:
        if Rb==orange:
            d2()
            r()
            d2()





    if Lb==white:
        if lB==green:
            b()
    if Lb==white:
        if lB==orange:
            di()
            b()
            d()
    if Lb==white:
        if lB==red:
            d()
            b()
            di()
    if Lb==white:
        if lB==blue:
            d2()
            b()
            d2()


    if Rb==white:
        if rB==green:
                bi()
    if Rb==white:
        if rB==red:
                d()
                bi()
                di()
    if Rb==white:
        if rB==orange:
                di()
                bi()
                d()
    if Rb==white:
        if rB==blue:
                d2()
                bi()
                d2()

def cross_d1(): #d layer, white oriented

    if Df==white:
        if dF==orange:
            f()
            d()
            fi()
            di()

    if Df==white:
        if dF==red:
            f()
            di()
            fi()
            d()
    if Df==white:
        if dF==green:
            f()
            d2()
            fi()
            d2()

    if Dl==white:
        if dL==blue:
            li()
            di()
            l()
            d()
    if Dl==white:
        if dL==green:
            li()
            d()
            l()
            di()
    if Dl==white:
        if dL==red:
            li()
            d2()
            l()
            d2()
    

    if Dr==white:
        if dR==blue:
            r()
            d()
            ri()
            di()
    if Dr==white:
        if dR==green:
            r()
            di()
            ri()
            d()

    if Dr==white:
        if dR==orange:
            r()
            d2()
            ri()
            d2()

    if Db==white:
        if dB==red:
            b()
            d()
            bi()
            di()
    if Db==white:
        if dB==orange:
            b()
            di()
            bi()
            d()
    if Db==white:
        if dB==blue:
            b()
            d2()
            bi()
            d2()

def cross_d2(): #d layer, white flipped

    if dF==white:
        if Df==red:
            fi()
            ri()

    if dF==white:
        if Df==orange:
            f()
            l()

    if dF==white:
        if Df==blue:
            fi()
            d()
            ri()
            di()

    if dF==white:
        if Df==green:
            f()
            d()
            l()
            di()

    if dL==white:
        if Dl==blue:
            li()
            fi()
    if dL==white:
        if Dl==green:
            l()
            b()
    if dL==white:
        if Dl==orange:
            li()
            d()
            fi()
            di()
    if dL==white:
        if Dl==red:
            li()
            di()
            fi()
            d()

    if dR==white:
        if Dr==blue:
            r()
            f()
    if dR==white:
        if Dr==green:
            ri()
            bi()
    if dR==white:
        if Dr==red:
            r()
            di()
            f()
            d()
    if dR==white:
        if Dr==orange:
            r()
            d()
            f()
            di()
    if dB==white:
        if Db==red:
            b()
            r()
    if dB==white:
        if Db==orange:
            bi()
            li()
    if dB==white:
        if Db==green:
            b()
            di()
            r()
            d()
    if dB==white:
        if Db==blue:
            b()
            d()
            r()
            di()

def cross_d0(): #orient d face
    if Df==white:
        if dF==orange:
            di()
    if Df==white:
        if dF==red:
            d()
    if Df==white:
        if dF==green:
            d2()
    if Dr==white:
        if dR==blue:
            di()
    if Dr==white:
        if dR==green:
            d()
    if Dr==white:
        if dR==orange:
            d2()
    if Dl==white:
        if dL==blue:
            d()
    if Dl==white:
        if dL==green:
            di()
    if Dl==white:
        if dL==red:
            d2()
    if Db==white:
        if dB==red:
            di()
    if Db==white:
        if dB==orange:
            d()
    if Db==white:
        if dB==blue:
            d2()
    

    

def cross_x1():
    
    cross_d0() #orient d layer at start
    cross_u1() #u layer, white oriented
    cross_u2() #u layer, white flipped
    
    cross_e1() #e layer, front 
    cross_e2() #e layer, back
   
    cross_d1() #d layer, white oriented
    cross_d2() #d layer, white flipped

def check_cross(): # checks cross

    if Df != white:
        cross_x1()
    if dF != blue:
        cross_x1()
    if Dl != white:
        cross_x1()
    if dL !=orange:
        cross_x1()
    if Dr != white:
        cross_x1()
    if dR != red:
        cross_x1()
    if Db != white:
        cross_x1()
    if dB != green:
        cross_x1()

def cross():    # if cross not solved, repeat cross_x1()

    write()
    t.write("/", font=("Arial", 20, "normal"))
    for _ in range(3):
        check_cross()
    
    
        
screen.onkey(cross,"c")

def tru_f2l():
    if urF==white and Urf==Ur==blue and uRf==uR==red:
        reversesexy()
    if ulF==white and Ulf==Ul==blue and uLf==uL==orange:
        reversesexy2()
    if uRf==white and Urf==Uf==red and urF==uF==blue:
        ui()
        fi()
        u()
        f()
    if uLf==white and Ulf==Uf==orange and ulF==uF==blue:
        u()
        f()
        ui()
        fi()
    if ulB==white and Ulb==Ul==green and uLb==uL==orange:
        u()
        l()
        ui()
        li()
    if urB==white and Urb==Ur==green and uRb==uR==red:
        ui()
        ri()
        u()
        r()
    if uLb==white and Ulb==Ub==orange and ulB==uB==green:
        ui()
        bi()
        u()
        b()
    if uRb==white and Urb==Ub==red and urB==uB==green:
        u()
        b()
        ui()
        bi()

    

def fl_u1(): #u layer, front

    if ulF==white:
        if Ulf==blue:
            
            f()
            u()
            fi()
    if ulF==white:
        if Ulf==red:
            ui()
            r()
            u()
            ri()
    if ulF==white:
        if Ulf==green:
            ri()
            u2()
            r()
    if ulF==white:
        if Ulf==orange:
            bi()
            u()
            b()

    if urF==white:
        if Urf==blue:
            fi()
            ui()
            f()
    if urF==white:
        if Urf==red:
            b()
            ui()
            bi()

    if urF==white:
        if Urf==orange:
            u()
            li()
            ui()
            l()
    if urF==white:
        if Urf==green:
            l()
            u2()
            li()

    if uLf==white:
        if Ulf==orange:
            li()
            ui()
            l()
    if uLf==white:
        if Ulf==blue:
            r()
            ui()
            ri()
    if uLf==white:
        if Ulf==red:
            b()
            u2()
            bi()

    if uLf==white:
        if Ulf==green:
            u()
            bi()
            ui()
            b()

    if uRf==white:
        if Urf==red:
            r()
            u()
            ri()
    if uRf==white:
        if Urf==blue:
            li()
            ui()
            l()
    if uRf==white:
        if Urf==orange:
            bi()
            u2()
            b()
    if uRf==white:
        if Urf==green:
            ui()
            b()
            u()
            bi()

    if Ulf==white:
        if ulF==orange:
            f()
            ui()
            fi()
            li()
            u2()
            l()
    if Ulf==white:
        if ulF==green:
            bi()
            u2()
            b2()
            li()
            bi()
            l()

    if Ulf==white:
        if ulF==blue:
            u()
            fi()
            ui()
            f2()
            ri()
            fi()
            r()

    if Ulf==white:
        if ulF==red:
            li()
            u()
            l()
            ri()
            ui()
            r()

    if Urf==white:
        if urF==red:
            fi()
            u()
            f()
            r()
            u2()
            ri()

    if Urf==white:
        if urF==blue:
            li()
            u2()
            l2()
            fi()
            li()
            f()
    if Urf==white:
        if urF==orange:
            bi()
            ui()
            b2()
            li()
            bi()
            l()

    if Urf==white:
        if urF==green:
            u()
            ri()
            ui()
            r2()
            bi()
            ri()
            b()

def fl_u2(): #u layer, back

    if urB==white:
        if Urb==blue:
            li()
            u2()
            l()

    if urB==white:
        if Urb==red:
            fi()
            u()
            f()
             
    if urB==white:
        if Urb==green:
            b()
            u()
            bi()
    if urB==white:
        if Urb==orange:
            ui()
            r()
            u()
            ri()

    if ulB==white:
        if Ulb==blue:
            r()
            u2()
            ri()
    if ulB==white:
        if Ulb==orange:
            f()
            ui()
            fi()

    if ulB==white:
        if Ulb==green:
            bi()
            ui()
            b()
    if ulB==white:
        if Ulb==red:
            u()
            ri()
            ui()
            r()

    if uRb==white:
        if Urb==red:
            ri()
            ui()
            r()
    if uRb==white:
        if Urb==green:
            l()
            ui()
            li()
    if uRb==white:
        if Urb==orange:
            f()
            u2()
            fi()
            
    if uRb==white: 
        if Urb==blue:
            u()
            fi()
            ui()
            f()

    if uLb==white:
        if Ulb==orange:
            l()
            u()
            li()
    if uLb==white:
        if Ulb==green:
            ri()
            u()
            r()
    if uLb==white:
        if Ulb==red:
            fi()
            u2()
            f()
    if uLb==white:
        if Ulb==blue:
            ui()
            f()
            ui()
            fi()

    if Urb==white:
        if uRb==red:
            ui()
            r()
            u()
            r2()
            f()
            r()
            fi()
    if Urb==white:
        if uRb==blue:
            u()
            bi()
            ui()
            b2()
            li()
            bi()
            l()
    if Urb==white:
        if uRb==orange:
            ui()
            l()
            ui()
            li()
            bi()
            u2()
            b()
    if Urb==white:
        if uRb==green:
            ri()
            u()
            r()
            b()
            u2()
            bi()

    if Ulb==white:
        if uLb==orange:
            u()
            li()
            ui()
            l2()
            fi()
            li()
            f()
    if Ulb==white:
        if uLb==blue:
            r()
            u()
            r2()
            f()
            r()
            fi()
    if Ulb==white:
        if uLb==red:
            ui()
            b()
            u()
            b2()
            r()
            b()
            ri()
    if Ulb==white:
        if uLb==green:
            bi()
            u()
            b()
            l()
            u2()
            li() 

def fl_d1(): # corner in front slot, white flipped
    if drF==white:
        if dRf==blue:
            r()
            ui()
            ri()
            u()
            r()
            ui()
            ri()
    if dRf==white:
        if drF==red:
            fi()
            ui()
            f()
            ui()
            fi()
            u()
            f()    
    if drF==white:
        if dRf != blue:
            fi()
            ui()
            f()
                
    if dRf==white:
        if drF != red:
            r()
            u()
            ri()    
        
    if dlF==white:
        if dLf != blue:
           f()
           u()
           fi()

    if dLf==white:
        if dlF != orange:
            li()
            ui()
            l()

    if dlF==white:
        if dLf==blue:
            li()
            u()
            l()
            ui()
            li()
            u()
            l()    
    if dLf==white:
        if dlF==orange:
            li()
            ui()
            l()
            u()
            li()
            ui()
            l()            

    


def fl_d2(): # corner in back slot, white flipped
    if dLb==white:
        if dlB==orange:
            bi()
            u()
            b()
            ui()
            bi()
            u()
            b()
    if dlB==white:
        if dLb==green:
            l()
            ui()
            li()
            u()
            l()
            ui()
            li()

    if dLb==white:
        if dlB != orange:
            l()
            u()
            li()
    if dlB==white:
        if dLb != green:
            bi()
            ui()
            b()

    if dRb==white:
        if drB==red:
            b()
            ui()
            bi()
            u()
            b()
            ui()
            bi()
        
    if drB==white:
        if dRb==green:
            ri()
            u()
            r()
            ui()
            ri()
            u()
            r()



    if dRb==white:
        if drB != red:
            ri()
            ui()
            r()
        
    if drB==white:
        if dRb != green:
            b()
            u()
            bi()

def fl_d3(): #wrong corner in slot, white oriented

    if Dlf==white:
        if dlF==red:
            li()
            ui()
            l()
            r()
            u()
            ri()
    if Dlf==white:
        if dlF==green:
            f()
            b()
            u2()
            fi()
            bi()
    if Dlf==white:
        if dlF==orange:
            f()
            u2()
            fi()
            l()
            ui()
            li()
    if Drf==white:
        if drF==orange:
            r()
            u()
            ri()
            li()
            ui()
            l()
    if Drf==white:
        if drF==red:
            fi()
            ui()
            f()
            b()
            u()
            bi()
    if Drf==white:
        if drF==green:
            l()
            r()
            u2()
            li()
            ri()
    if Dlb==white:
        if dLb==blue:
            bi()
            ui()
            b()
            f()
            u()
            fi()
    if Dlb==white:
        if dLb==red:
            l()
            r()
            u2()
            li()
            ri()
    if Dlb==white:
        if dLb==green:
            l()
            u()
            li()
            ri()
            ui()
            r()
    if Drb==white:
        if dRb==orange:
            li()
            ri()
            u2()
            l()
            r()
    if Drb==white:
        if dRb==blue:
            b()
            u()
            bi()
            fi()
            ui()
            f()
    if Drb==white:
        if dRb==green:
            ri()
            ui()
            r()
            l()
            u()
            li()
    
def f2l_u(): #edge on top

    if Uf==blue:
        if uF==red:
            u2()
            sledgehammer()
            r()
            u()
            ri()
    if Uf==blue:
        if uF==orange:
            u2()
            sledgehammer2()
            li()
            ui()
            l()
    if Uf==red:
        if uF==green:
            u()
            bi()
            r()
            b()
            ri()
            b()
            u()
            bi()
    if Uf==red:
        if uF==blue:
            u()
            f()
            ri()
            fi()
            r()
            fi()
            ui()
            f()
    if Uf==green:
        if uF==orange:
            li()
            b()
            l()
            bi()
            l()
            u()
            li()
    if Uf==green:
        if uF==red:
            r()
            bi()
            ri()
            b()
            ri()
            ui()
            r()
    if Uf ==orange:
        if uF==blue:
            ui()
            fi()
            l()
            f()
            li()
            f()
            u()
            fi()
    if Uf==orange:
        if uF==green:
            ui()
            b()
            li()
            bi()
            l()
            bi()
            ui()
            b()
    
    if Ul==red:
        if uL==green:
            bi()
            r()
            b()
            ri()
            b()
            u()
            bi()
    if Ul==red:
        if uL==blue:
            r()
            ui()
            ri()
            ui()
            fi()
            u()
            f()
    if Ul==blue:
        if uL==red:
            ui()
            sledgehammer()
            r()
            u()
            ri()
    if Ul==blue:
        if uL==orange:
            u()
            sledgehammer2()
            li()
            ui()
            l()
    if Ul==orange:
        if uL==green:
            u2()
            l()
            ui()
            li()
            ui()
            bi()
            u()
            b()
    if Ul==orange:
        if uL==blue:
            u2()
            li()
            u()
            l()
            u()
            f()
            ui()
            fi()
    if Ul==green:
        if uL==orange:
            ui()
            bi()
            u()
            b()
            u()
            l()
            ui()
            li()
    if Ul==green:
        if uL==red:
            ui()
            b()
            ui()
            bi()
            ui()
            ri()
            u()
            r()
           
    if Ur==orange:
        if uR==blue:
            li()
            u()
            l()
            u()
            f()
            ui()
            fi()
    if Ur==orange:
        if uR==green:
            l()
            ui()
            li()
            ui()
            bi()
            u()
            b()
    if Ur==blue:
        if uR==red:
            ui()
            fi()
            u()
            f()
            u()
            r()
            ui()
            ri()
    if Ur==blue:
        if uR==orange:
            ui()
            f()
            ui()
            fi()
            ui()
            li()
            u()
            l()
    if Ur==red:
        if uR==green:
            u2()
            ri()
            u()
            r()
            u()
            b()
            ui()
            bi()
    if Ur==red:
        if uR==blue:
            u2()
            r()
            ui()
            ri()
            ui()
            fi()
            u()
            f()
    if Ur==green:
        if uR==orange:
            u()
            bi()
            u()
            b()
            u()
            l()
            ui()
            li()
    if Ur==green:
        if uR==red:
            u()
            b()
            ui()
            bi()
            ui()
            ri()
            u()
            r()
    
    if Ub==blue:
        if uB==red:
            sledgehammer()
            r()
            u()
            ri()
    if Ub==blue:
        if uB==orange:
            sledgehammer2()
            li()
            ui()
            l()
    if Ub==red:
        if uB==green:
            ui()
            ri()
            u()
            r()
            u()
            b()
            ui()
            bi()
    if Ub==red:
        if uB==blue:
            ui()
            r()
            ui()
            ri()
            ui()
            fi()
            u()
            f()
    if Ub==green:
        if uB==red:
            u2()
            b()
            ui()
            bi()
            ui()
            ri()
            u()
            r()
    if Ub==green:
        if uB==orange:
            u2()
            bi()
            u()
            b()
            u()
            l()
            ui()
            li()
    if Ub==orange:
        if uB==blue:
            u()
            li()
            u()
            l()
            u()
            f()
            ui()
            fi()
    if Ub==orange:
        if uB==green:
            u()
            l()
            ui()
            li()
            ui()
            bi()
            u()
            b()
        
def f2l_e1(): #edge flipped, in slot

    if lF==orange:
        if Lf==blue:
            li()
            u()
            l()
            ui()
            f()
            u2()
            fi()
            u2()
            f()
            ui()
            fi()
    if rF==red:
        if Rf==blue:
            r()
            ui()
            ri()
            u()
            fi()
            u2()
            f()
            u2()
            fi()
            u()
            f()
    if Rb==green:
        if rB==red:
            b()
            ui()
            bi()
            u()
            ri()
            u2()
            r()
            u2()
            ri()
            u()
            r()
    if Lb==green:
        if lB==orange:
            l()
            ui()
            li()
            u()
            bi()
            u2()
            b()
            u2()
            bi()
            u()
            b()


def f2l_e2(): #edge in wrong slot
    
    if lF != blue:
        sledgehammer2()
        li()
        ui()
        l()
    if Lf != orange:
        sledgehammer2()
        li()
        ui()
        l()
    if rF != blue:
        sledgehammer()
        r()
        u()
        ri()
    if Rf != red:
        sledgehammer()
        r()
        u()
        ri()    
    if lB != green:
        li()
        b()
        l()
        bi()
        l()
        u()
        li()
    if Lb != orange:
        li()
        b()
        l()
        bi()
        l()
        u()
        li()
    if rB != green:
        r()
        bi()
        ri()
        b()
        ri()
        ui()
        r()
    if Rb != red:
        r()
        bi()
        ri()
        b()
        ri()
        ui()
        r()
    

def fl_x1():

    fl_u1()
    fl_u2()
    fl_d1()
    fl_d2()
    
    fl_d3()

    fl_u1()
    fl_u2()
    fl_d1()
    fl_d2()

def check_fl():

    if Dlf != white:
        fl_x1()
    if Drf != white:
        fl_x1()
    if Dlb != white:
        fl_x1()
    if Drb != white:
        fl_x1()
    if dlF != blue:
        fl_x1()
    if drF != blue:
        fl_x1()
    if dLf != orange:
        fl_x1()
    if dLb != orange:
        fl_x1()
    if dlB != green:
        fl_x1()
    if drB != green:
        fl_x1()
    if dRb != red:
        fl_x1()
    if dRf != red:
        fl_x1()
        

def fl():
    for _ in range(3):
        check_fl()

def f2l_x1():
    for _ in range(4):
        tru_f2l()
        f2l_u()
    tru_f2l()
    f2l_e2()
    for _ in range(2):
        tru_f2l()
        f2l_u()
    f2l_e1()
    tru_f2l()
    
def check_f2l():

    if lF != blue:
        f2l_x1()
    if Lf != orange:
        f2l_x1()
    if rF != blue:
        f2l_x1()
    if Rf != red:
        f2l_x1()    
    if lB != green:
        f2l_x1()
    if Lb != orange:
        f2l_x1()
    if rB != green:
        f2l_x1()
    if Rb != red:
        f2l_x1()
  

screen.onkey(fl,"1")
      
def f2l():
    for _ in range(5):
        check_f2l()

screen.onkey(f2l, "2")




def scramble_x1():
    choice = ["u","ui","r","ri","f","fi","d","di","l","li","b","bi"]
    selected = random.choice(choice)
    
    if selected == "u":
        u()
    if selected == "ui":
        ui()
    if selected == "r":
        r()  
    if selected == "ri":
        ri()  
    if selected == "f":
        f()
    if selected == "fi":
        fi()
    if selected == "d":
        d()
    if selected == "di":
        di()
    if selected == "l":
        l()
    if selected == "li":
        li()
    if selected == "b":
        b()
    if selected == "bi":
        bi()
    



def scramble_x10():
    for _ in range(10):
        scramble_x1()

screen.onkey(scramble_x10,"8")

def scramble20():
    for _ in range(20):
        scramble_x1()
    

screen.onkey(scramble20,"9")

def dot1(): 
    r()
    u2()
    ri()
    sledgehammer()
    u2()
    sledgehammer()
def dot2():

    f()
    sexymove()
    fi()
    b()
    u()
    l()
    ui()
    li()
    bi()
def dot3():
    #f (R U R' U') f' U' F (R U R' U') F'
    b()
    u()
    l()
    ui()
    li()
    bi()
    ui()
    f()
    sexymove()
    fi()
def dot4():
    #f (R U R' U') f' U F (R U R' U') F' 
    b()
    u()
    l()
    ui()
    li()
    bi()
    u()
    f()
    sexymove()
    fi()
def dot17(): 

    r()
    u()
    ri()
    u()
    sledgehammer()
    u2()
    sledgehammer()
def dot18():
    #y R U2' (R2' F R F') U2' M' (U R U' r')
    r()
    u2()
    ri()
    sledgehammer()
    u2() 
    l()
    ri()
    f()
    r()
    fi()
    li()
def dot19():
    #M U (R U R' U') M' (R' F R F') 
    li()
    r()
    b()
    r()
    b()
    ri()
    bi()
    l()
    ri()
    sledgehammer()

def fishshape9(): 
    
    sexymove()
    ri()
    f()
    r()
    sexymove()
    fi()
def fishshape10(): 
    
    r()
    u()
    ri()
    u()
    sledgehammer()
    r()
    u2()
    ri()

def catchinggame():

    f()
    r()
    ui()
    ri()
    ui()
    r()
    u()
    ri()
    fi()


def sune():

    r()
    u()
    ri()
    u()
    r()
    u2()
    ri()
def sune2():

    r()
    u2()
    ri()
    ui()
    r()
    ui()
    ri()

def hcross():

    r()
    u2()
    ri()
    ui()
    sexymove()
    r()
    ui()
    ri()
def archer_cross():

    r()
    u2()
    r2()
    ui()
    r2()
    ui()
    r2()
    u2()
    r()

def fat_cross():

    ri()
    fi()
    l()
    f()
    r()
    fi()
    li()
    f()
def cloud_cross():

    ri()
    f()
    r()
    bi()
    ri()
    fi()
    r()
    b()
  
def superman():

    r2()
    d()
    ri()
    u2()
    r()
    di()
    ri()
    u2()
    ri()

def easy_t():

    f()
    sexymove()
    fi()
def easy_t2():

    fi()
    sexymove2()
    f()

def fast_t():
    sexymove()
    sledgehammer()
def fast_t2():
    sexymove2()
    sledgehammer2()

def pshape31():
              
    ri()
    ui()
    f()
    reversesexy()
    fi()
    r()
def pshape32():
    l()
    u()
    fi()
    reversesexy2()
    f()
    li()
def pshape43():
     
    fi()
    ui()
    li()
    u()
    l()
    f()
def pshape44():

    f()
    u()
    r()
    ui()
    ri()
    fi()

def solve_oll_dot(): #direct solve
    if uF==uL==uR==uB==uLb==uLf==uRb==uRf==yellow:
        dot1()
    if uF==uL==uR==uB==uLf==uLb==urF==urB==yellow:
        dot2()
    if uF==uL==uR==uB==Urf==uRb==uLf==ulB==yellow:
        dot3()
    if uF==uL==uR==uB==Urb==uRf==ulF==uLb==yellow:
        dot4()
    if uF==uL==uR==uB==Ulb==Urf==urB==uLf==yellow:
        dot17()
    if uF==uL==uR==uB==Urb==Urf==uLb==uLf==yellow:
        dot18()
    if uF==uL==uR==uB==Ulb==Urb==uLf==uRf==yellow:
        dot19()
    
def solve_oll_l(): #direct solve

    if Ul==Ub==Ulb==Ulf==uF==uR==uRf==uRb:
        pshape44()
    if Ur==Ub==Urb==Urf==uF==uL==uLf==uLb:
        pshape43()
    if Ur==Ub==Urb==Urf==uF==ulF==uL==ulB:
        pshape31()
    if Ul==Ub==Ulb==Ulf==uF==urF==uR==urB:
        pshape32()
    if Ul==Ub==Ulb==Urf==uF==uR==ulF==uRb:
        catchinggame()
    
def solve_oll_bar():    #direct solve
    
    if Ul==Ur==Urb==Urf==ulF==ulB==uF==uB:
        fast_t()
    if Ul==Ur==Ulb==Ulf==uF==uB==urF==urB:
        fast_t2()

    if Ul==Ur==Ulb==Ulf==uF==uB==uRf==uRb:
        easy_t2()
    

def create_ollcross_l(): #create cross from l
    if Ul==Ub==uF==uR:
        f()
        reversesexy()
        fi()
    if Uf==Ul==uR==uB:
        u()
        f()
        reversesexy()
        fi()
    if Uf==Ur==uL==uB:
        u2()
        f()
        reversesexy()
        fi()
    if uF==uL==Ur==Ub:
        ui()
        f()
        reversesexy()
        fi()
    
def create_ollcross_bar(): #create cross from bar
    if Ul==Ur==uF==uB:
        f()
        sexymove()
        fi()
    if Uf==Ub==uL==uR:
        u()
        f()
        sexymove()
        fi()

def solve_ollcross():
    if Uf==Ul==Ur==Ub==Ulf==urF==uRb==ulB:
        sune()
    if Uf==Ul==Ur==Ub==Urb==uLb==ulF==uRf:
        sune2()
    if Uf==Ul==Ur==Ub==ulF==urF==ulB==urB:
        hcross()
    if Uf==Ul==Ur==Ub==Ulf==Ulb==urF==urB:
        fat_cross()
    if Uf==Ul==Ur==Ub==Ulb==Urf==ulF==uRb:
        cloud_cross()
    if Uf==Ul==Ur==Ub==Ulb==Urb==ulF==urF:
        superman()
    if Uf==Ul==Ur==Ub==uLf==uLb==urF==urB:
        archer_cross()
    
    
def solve_oll():
    solve_oll_dot()         #direct solve dot
    solve_oll_l()           #direct solve l
    solve_oll_bar()         #direct solve bar
    create_ollcross_l()     #create cross from l
    create_ollcross_bar()   #create cross from bar
    solve_ollcross()        #solve cross

screen.onkey(solve_oll,"3")

def check_oll():
    solve_oll()
    if Uf != yellow:
        u()
        solve_oll()
    if Ul != yellow:
        u()
        solve_oll()
    if Ur != yellow:
        u()
        solve_oll()
    if Ub != yellow:
        u()
        solve_oll()
    if Ulf != yellow:
        u()
        solve_oll()
    if Urf != yellow:
        u()
        solve_oll()
    if Ulb != yellow:
        u()
        solve_oll()
    if Urb != yellow:
        u()
        solve_oll()

def oll():
    check_oll()
    check_oll()
    check_oll()
    









def tperm():

    sexymove()
    ri() 
    f()
    r2()
    ui()
    ri()
    ui()
    r()
    u()
    ri()
    fi()
    

def jperm1():

    r()
    u()
    ri()
    fi()
    sexymove()
    ri()
    f()
    r2()
    ui()
    ri()

def jperm2():

    li()
    ui()
    l()
    f()
    sexymove2()
    l()
    fi()
    l2()
    u()
    l()

def yperm():
    f()
    r()
    ui()
    ri()
    ui()
    r()
    u()
    ri()
    fi()
    sexymove()
    sledgehammer()

def aperm():

    ri()
    f()
    ri()
    b2()
    r()
    fi()
    ri()
    b2()
    r2()

def aperm2():

    r2()
    b2()
    r()
    f()
    ri()
    b2()
    r()
    fi()
    r()

def rperm():

    r()
    ui()        
    ri()
    ui()
    r()
    u()
    r()
    d()
    ri()
    ui()
    r()
    di()
    ri()
    u2()
    ri()
    
def rperm2():

    ri()
    u2()
    r()
    u2()
    ri()
    f()
    sexymove()
    ri()
    fi()
    r2()

def fperm():

    ri()
    ui()
    fi()
    sexymove()
    ri()
    f()
    r2()
    ui()
    ri()
    ui()
    r()
    u()
    ri()
    u()
    r()

def uperm():
    #(R U' R U) R U (R U' R' U') R2
    r()
    ui()
    r()
    u()
    r()
    u()
    r()
    ui()
    ri()
    ui()
    r2()

def uperm2():
    #R2 U (R U R' U') R' U' (R' U R')
    r2()
    u()
    sexymove()
    ri()
    ui()
    ri()
    u()
    ri()

def vperm():

    #R' U R' U' R D' R' D R' U D' R2 U' R2 D R2
    ri()
    u()
    ri()
    ui()
    r()
    di()
    ri()
    d()
    ri()
    u()
    di()
    r2()
    ui()
    r2()
    d()
    r2()

def gperm():
    #R2 U (R' U R' U') (R U' R2) D U' (R' U R D') [U]
    r2()
    u()
    ri()
    u()
    ri()
    ui()
    r()
    ui()
    r2()
    d()
    ui()
    ri()
    u()
    r()
    di()

def gperm2():

    ri()
    ui()
    r()
    u()
    di()
    r2()
    u()
    ri()
    u()
    r()
    ui()
    r()
    ui()
    r2()
    d()

def gperm3():

    r2()
    ui()
    r()
    ui()
    r()
    u()
    ri()
    u()
    r2()
    di()
    u()
    r()
    ui()
    ri()
    d()

def gperm4():
     
     r()
     u()
     ri()
     ui()
     d()
     r2()
     ui()
     r()
     ui()
     ri()
     u()
     ri()
     u()
     r2()
     di()

def zperm():
    
    #U2 (R U R' U)(R' U' R' U)(R U' R' U')R2 U R
    u2()
    r()
    u()
    ri()
    u()
    ri()
    ui()
    ri()
    u()
    r()
    ui()
    ri()
    ui()
    r2()
    u()
    r()

def eperm():
    #x' (R U' R' D) (R U R' D') (R U R' D) (R U' R' D') x
    r()
    bi()
    ri()
    f()
    r()
    b()
    ri()
    fi()
    r()
    b()
    ri()
    f()
    r()
    bi()
    ri()
    fi()


def hperm():
    l2()
    r2()
    d()
    l2()
    r2()
    u2()
    l2()
    r2()
    d()
    l2()
    r2()



def nperm():
    #(RUR'U)(RUR'F')(RUR'U')(R'FR2U') R' U2 (RU'R')
    r()
    u()
    ri()
    u()
    r()
    u()
    ri()
    fi()
    sexymove()
    ri()
    f()
    r2()
    ui()
    ri()
    u2()
    r()
    ui()
    ri()

def nperm2():

    li()
    ui()
    l()
    ui()
    li()
    ui()
    l()
    f()
    sexymove2()
    l()
    fi()
    l2()
    u()
    l()
    u2()
    li()
    u()
    l()



def solve_pll():

    if uLb==uLf==uR:
        if ulF==uF==uRb:
            if ulB==uB==uRf:
                tperm()
    if uLf==uL==uLb:
        if uF==urF==urB:
            if ulF==uR==uRb:
                jperm1()
    if uRf==uR==uRb:
        if ulF==uF==ulB:
            if uLb==uL==urF:
                jperm2()
    if uL==uLf==uRf:
        if ulF==uF==uRb:
            if ulB==urB==uR:
                aperm()
    if uL==uLf==urB:
        if ulF==uF==ulB:
            if uRf==uRb==uB:
                aperm2()
    if ulF==uF==ulB:
        if uR==uRb==uLb:
            yperm()
    if ulF==uF==uRb:
        if uLf==uLb==uB:
            rperm()
    if ulF==urF==uR:
        if uL==uLf==urB:
            rperm2()
    if uR==uLb==uLf:
        if uRb==uRf==uF:
            if urB==uB==ulB:
                uperm()
    if uL==uRb==uRf:
        if uLb==uLf==uF:
            if urB==uB==ulB:
                if ulF==urF==uR:
                    uperm2()
    if uLb==uL==uLf:
        if uR==urF==urB:
            fperm()
    if uLf==uLb==uR:
        if uF==urF==urB:
            if uL==ulB==uRf:
                gperm()
    if uLf==uLb==uB:
        if ulF==uR==uRb:
            if uL==urF==urB:
                gperm2()
    if uLf==uLb==uR:
        if uB==urB==urF:
            if uL==ulF==uRb:
                gperm3()
    if uLf==uLb==uF:
        if uRf==uR==ulB:
            if uL==urF==urB:
                gperm4()
    if ulF==uF==ulB:
        if uLf==uL==uRf:
            if urF==uR==urB:
                vperm()

    if ulF==urF==uR:
        if uF==uRf==uRb:
            zperm()
    if uF==uLb==uRb:
        if uB==uLf==uRf:
            if uR==urF==urB:
                eperm()
    if ulF==urF==uB:
        if uLf==uLb==uR:
            if uRf==uRb==uL:
                hperm()
    if uF==urF==urB:
        if uR==uRb==uLb:
            if uL==uLf==uRf:
                nperm()
    if uF==ulF==ulB:
        if uR==uRf==uLf:
            if uL==uLb==uRb:
                nperm2()
    
def check_pll(): 
    solve_pll()
    AUF()
    if ulF != uF:
        u()
        solve_pll()
    if uF != urF:
        u()
        solve_pll()
    if ulF != urF:
        u()
        solve_pll()
    if uRf != uR:
        u()
        solve_pll()
    if uR != uRb:
        u()
        solve_pll()
    if uRf != uRb:
        u()
        solve_pll()
    
    
    
    
def pll():
    for _ in range(3):
        check_pll()
    AUF()
                
screen.listen()
screen.onkey(pll,"4") 

def AUF():
    if ulF==uF==urF==orange:
        if uRf==uR==uRb==blue:
            u()
    if ulF==uF==urF==red:
        if uRf==uR==uRb==green:
            ui()
    if ulF==uF==urF==green:
        if uRf==uR==uRb==orange:
            u2()


def countmoves():
    
    global m
    m=m+1
    global m2
    m2=m2+1
    

def resetmoves_neg1():
    global m
    m=-1
    
def resetmoves_0():
    global m
    m=0
    global m2
    m2=0
def reset_m2():
    global m2
    m2=0 


screen.onscreenclick(help,1)

def showmoves(x,y,text):
    
    t.pu()
    t.goto(x,y)
    t.pd()
    t.color("white","white") 
    t.begin_fill()
    t.fd(80); t.lt(90)
    t.fd(50); t.lt(90)
    t.fd(80); t.lt(90)
    t.fd(50); t.lt(90)
    t.end_fill()  
    t.pencolor("black")
    t.write(text, font=("Arial", 30, "bold"))

def subtext(x,y,subtext):

    t.pu()
    t.setpos(x, y-20)
    t.pd()
    t.pencolor("black")
    t.write(subtext,font=("arial", 15, "normal"))
    screen.update()

def drawzero(x,y):
    t.pu()
    t.setpos(x, y)
    t.pd()
    t.pencolor("black")
    t.write("0",font=("arial", 30, "bold"))
    screen.update()

timeflag = True
def timer():
    start_time = time.time()
    
    while timeflag == True:
        time.sleep(1)
        end_time = time.time()
        showmoves(160,250,round(end_time - start_time))
        #showmoves(160,250,(((end_time - start_time)//0.1)/10))
        #print(round(end_time - start_time))
        

timerThread = threading.Thread(target=timer)    

def write2(x,y,text,fontsize=15,style = 'normal'):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.write(text,font=("arial", fontsize, style))

def instructions():
    instructioncount = 0
    y = 300
    texts = ("Type:","Scramble + Solve:",'8 = 10 move scramble','9 = 20 move scramble','space = solve',
    "Manual Moves:","u = up ↻","r = right ↻ ","l = left ↻","f = front ↻","d = down ↻","b = back ↻",
    "shift + u = up ↺","shift + r = right ↺ ","shift + l = left ↺","shift + f = front ↺",
    "shift + d = down ↺","shift + b = back ↺",
    '↻ = clockwise','↺ = counterclockwise')
    for text in texts:
        if instructioncount == 0 or instructioncount == 1 or instructioncount == 5:
            write2(-550,y,text,15,'bold')
            y = y - 30
            instructioncount +=1
        else:
            write2(-550,y,text,15)
            y = y - 30
            instructioncount +=1
    



def solve():
    global showmovesflag
    showmovesflag=1
    resetmoves_0()
    global timerThread
    if not timerThread.is_alive():
        timerThread.start()
    cross()
    
    reset_m2()
    tru_f2l()
    fl()
    f2l()
    
    reset_m2()
    oll()
    
    reset_m2()
    pll()
    AUF()
    global timeflag
    timeflag = False
    

screen.onkey(solve, "space")

def reset():
    t.clear()
    global x
    x=-390
    global y
    y=-200
    global showmovesflag
    showmovesflag=0
    resetmoves_neg1()
    #explain("royalblue")
    global dlF, dF, drF, lF, F, rF, ulF, uF, urF 
    dlF, dF, drF, lF, F, rF, ulF, uF, urF =[blue for _ in range(9)] #front 
    global dRf, dR, dRb, Rf, R, Rb, uRf, uR, uRb
    dRf, dR, dRb, Rf, R, Rb, uRf, uR, uRb=[red for _ in range(9)] #right 
    global dLb, dL, dLf, Lb, L, Lf, uLb, uL, uLf
    dLb, dL, dLf, Lb, L, Lf, uLb, uL, uLf=[orange for _ in range(9)] #left 
    global dlB, dB, drB, lB, B, rB, ulB, uB, urB
    dlB, dB, drB, lB, B, rB, ulB, uB, urB=[green for _ in range(9)] #back
    global Ulf, Uf, Urf, Ul, U, Ur, Ulb, Ub, Urb
    Ulf, Uf, Urf, Ul, U, Ur, Ulb, Ub, Urb=[yellow for _ in range(9)] #up
    global Dlb, Db, Drb, Dl, D, Dr, Dlf, Df, Drf
    Dlb, Db, Drb, Dl, D, Dr, Dlf, Df, Drf=[white for _ in range(9)] #down
    drawCube()
    instructions()


#actions


reset()
subtext(160,250,"time")
subtext(250,250,"scramble")
subtext(250,175,"solve")
drawzero(160,250)
drawzero(250,175)


screen.listen()
screen.update()
screen.mainloop()
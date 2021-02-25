import numpy as np

# =============================================================

import os
import turtle
import random
import time 
os.system('clear')
t=turtle.Turtle()
t.hideturtle()
t.pensize(5)
t.speed(2)
screen = turtle.Screen()
screen.setup(900,900)
screen.tracer(10,10)
drawflag = False
side = 70
grass = 'white'
fire = 'red'
gold = 'gold'

class Square:
    def __init__(self, x, y, fillcolor, rwd, num):
        self.x = x 
        self.y = y 
        self.fillcolor = fillcolor
        self.rwd = rwd
        self.num = num

    def draw(self):
        t.penup()
        t.goto(self.x,self.y)
        t.pendown()
        t.color("black",self.fillcolor) 
        t.begin_fill()
        for _ in range(4):
            t.fd(side); t.lt(90)
        t.end_fill()    
        #time.sleep(1)
    def draw_num(self):
        t.penup()
        t.goto(self.x+10,self.y+10)
        t.pendown()
        t.write(self.num, font=("Arial", 20, "bold"))
    def draw_outline(self):
        t.penup()
        t.goto(self.x,self.y)
        t.pendown()
        t.pencolor('turquoise') 
        for _ in range(4):
            t.fd(side); t.lt(90)
    @staticmethod
    def find(x,y):
        for square in li_objects:
            if square.x == x and square.y == y:
                return square
 
d = {}
for y in range(3):
    for x in range(3):
        d[3*y+x] = Square(x*side,-y*side,grass,-0.1,3*y+x)
        d[3*y+x].draw()
        d[3*y+x].draw_num()
print(d)  
li_objects = [d[key] for key in d] #objects '<__main__.Square object at 0x10c03f1c0>'
li_keys = [key for key in d] #keys '25'

def mouseclick(x,y):
    
  square = Square.find(x-x%side,y-y%side)
  if square.fillcolor == fire:
      square.fillcolor = grass
      square.rwd = -0.1
  else:
    square.fillcolor = fire
    square.rwd = -5
  print('mc1')
  square.draw()
  square.draw_num()
  screen.update()

screen.onclick(mouseclick,1)

def mouseclick2(x,y):
  square = Square.find(x-x%side,y-y%side)
  if square.fillcolor == gold:
      square.fillcolor = grass
      square.rwd = -0.1
  else:
      square.fillcolor = gold
      square.rwd = 3

  square.draw()
  square.draw_num()
  screen.update()

screen.onclick(mouseclick2,2)


def my_print(Q):
  # hard-coded hack for this problem only
  rows = len(Q); cols = len(Q[0])
  print("       0      1      2      3      4      5\
      6      7      8")
  for i in range(rows):
    print("%d " % i, end="")
    if i < 10: print(" ", end="")
    for j in range(cols): print(" %6.2f" % Q[i,j], end="")
    print("")
  print("")

def get_poss_next_states(s, F, ns):
  # given a state s and a feasibility matrix F
  # get list of possible next states
  poss_next_states = []
  for j in range(ns):
    if F[s,j] == 1: poss_next_states.append(j)
  return poss_next_states

def get_rnd_next_state(s, F, ns):
  # given a state s, pick a feasible next state
  poss_next_states = get_poss_next_states(s, F, ns)
  next_state = \
    poss_next_states[np.random.randint(0,\
    len(poss_next_states))]
  return next_state 

print(d[1].rwd)
# =============================================================

def train(F, R, Q, gamma, lrn_rate, goal, ns, max_epochs):
  # compute the Q matrix
  for i in range(0,max_epochs):
    curr_s = np.random.randint(0,ns)  # random start state

    while(True):
      next_s = get_rnd_next_state(curr_s, F, ns)
      poss_next_next_states = \
        get_poss_next_states(next_s, F, ns)

      max_Q = -9999.99
      for j in range(len(poss_next_next_states)):
        nn_s = poss_next_next_states[j]
        q = Q[next_s,nn_s]
        if q > max_Q:
          max_Q = q
      # Q = [(1-a) * Q]  +  [a * (rt + (g * maxQ))]
      Q[curr_s][next_s] = ((1 - lrn_rate) * Q[curr_s] \
        [next_s]) + (lrn_rate * (R[curr_s][next_s] + \
        (gamma * max_Q)))

      curr_s = next_s
      if curr_s == goal: break

# =============================================================

def walk(start, goal, Q):
  # go to goal from start using Q
  curr = start
  print(str(curr) + "->", end="")
  x = 0
  d[0].fillcolor = 'turquoise'
  #d[0].draw()
  d[0].draw_outline()
  #d[0].draw_num()
  t.penup()
  t.goto(x,100)
  t.pendown()
  t.write("0->",font=("Arial", 30, "bold"))
  while curr != goal:
    x += 50
    next = np.argmax(Q[curr])
    print(str(next) + "->", end="")
    t.penup()
    t.goto(x,100)
    t.pendown()
    t.write(str(next) + "->",font=("Arial", 30, "bold"))
    
    d[int(next)].fillcolor = 'turquoise'
    d[int(next)].draw_outline()
    #d[int(next)].draw()
    #d[int(next)].draw_num()
    curr = next
    
  print("done")
  t.penup()
  t.goto(x+50,100)
  t.pendown()
  t.write("done",font=("Arial", 30, "bold"))
# =============================================================

def main():
  np.random.seed(1)
  print("\nSetting up maze in memory")
 
  
  x = 1

  F = np.zeros(shape=[9,9], dtype=np.int)  # Feasible 
  R = np.zeros(shape=[9,9], dtype=np.int)  # Rewards
  for i in range(3):
    F[i,i+3] = x; F[i+3,i] = x
    F[i+3,i+6] = x; F[i+6,i+3] = x

    F[3*i,3*i+1] = x; F[3*i+1,3*i] = x
    F[3*i+1,3*i+2] = x; F[3*i+2,3*i+1] = x
    
    R[i,i+3] = d[i+3].rwd; R[i+3,i] = d[i].rwd
    R[i+3,i+6] = d[i+6].rwd; R[i+6,i+3] = d[i+3].rwd

    R[3*i,3*i+1] = d[3*i+1].rwd; R[3*i+1,3*i] = d[3*i].rwd
    R[3*i+1,3*i+2] = d[3*i+2].rwd; R[3*i+2,3*i+1] = d[3*i+1].rwd
    #print(F[i,i+3])
  R[5,8] = 10; R[7,8] = 10

# =============================================================

  Q = np.zeros(shape=[9,9], dtype=np.float32)  # Quality
  
  print("Analyzing maze with RL Q-learning")
  start = 0; goal = 8 #start and end
  ns = 9  # number of states
  gamma = 0.8
  lrn_rate = 0.5
  max_epochs = 1000
  train(F, R, Q, gamma, lrn_rate, goal, ns, max_epochs)
  print("Done ")
  
  print("The Q matrix is: \n ")
  my_print(Q)

  print("Using Q to go from 0 to goal (3)")

  walk(start, goal, Q)
screen.onkey(main,'space')  
#if __name__ == "__main__":
#  main()

screen.listen()
screen.update()
screen.mainloop()
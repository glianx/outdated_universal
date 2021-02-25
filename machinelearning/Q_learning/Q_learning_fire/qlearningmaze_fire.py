import numpy as np
import os
import turtle
import random
import time 
start_time = time.time()
os.system('clear')
t=turtle.Turtle()
t.hideturtle()
t.pensize(5)
t.speed(2)
screen = turtle.Screen()
screen.setup(1500,900)
screen.tracer(10,10)
drawflag = False
side = 60

grass = 'white'
fire = 'red'
gold = 'gold'

grass_rwd = 1
fire_rwd = -20
gold_rwd = 10
end_rwd = 100

n = 6
class Square:
    def __init__(self, x, y, fillcolor, rwd, num):
        self.x = x - 5*side
        self.y = y + 4*side
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


# =============================================================


d = {}
for y in range(n):
    for x in range(n):
        d[n*y+x] = Square(x*side,-y*side,grass,-0.1,n*y+x)
        d[n*y+x].draw()
        d[n*y+x].draw_num()
li_objects = [d[key] for key in d] #objects '<__main__.Square object at 0x10c03f1c0>'
li_keys = [key for key in d] #keys '25'


# =============================================================


def restart():
    t.clear()
    d = {}
    for y in range(n):
        for x in range(n):
            d[n*y+x] = Square(x*side,-y*side,grass,-0.1,n*y+x)
            d[n*y+x].draw()
            d[n*y+x].draw_num()
    li_objects = [d[key] for key in d] #objects '<__main__.Square object at 0x10c03f1c0>'
    li_keys = [key for key in d] #keys '25'

screen.onkey(restart,"0")

def mouseclick(x,y):
    
  square = Square.find(x-x%side,y-y%side)
  if square.fillcolor == fire:
      square.fillcolor = grass
      square.rwd = -10
  else:
    square.fillcolor = fire
    square.rwd = fire_rwd
  square.draw()
  square.draw_num()
  screen.update()

screen.onclick(mouseclick,1)

def mouseclick2(x,y):
  square = Square.find(x-x%side,y-y%side)
  if square.fillcolor == gold:
      square.fillcolor = grass
      square.rwd = -1
  else:
      square.fillcolor = gold
      square.rwd = gold_rwd

  square.draw()
  square.draw_num()
  screen.update()

screen.onclick(mouseclick2,2)

def goto(x,y):
  t.penup()
  t.goto(x,y)
  t.pendown()

def write(text, x, y):
  goto(x,y)
  t.write(text,font = ("Arial", 30, "normal"))

# =============================================================


def my_print(Q):

  print('len Q = ',len(Q))
  if n < 5:
    rows = len(Q); cols = len(Q[0])
    print("       0      1      2      3      4      5\
      6      7      8      9      10     11 \
    12     13     14     15")
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



# =============================================================

def train(F, R, Q, gamma, lrn_rate, goal, ns, max_epochs):
  # compute the Q matrix
  for i in range(0,max_epochs):
    curr_s = np.random.randint(0,ns)  # random start state
    #loop_control = 0
    while(True):
      next_s = get_rnd_next_state(curr_s, F, ns)
      poss_next_next_states = get_poss_next_states(next_s, F, ns)
      
      max_Q = -9999.99
      #for j in range(len(poss_next_next_states)):
      #  nn_s = poss_next_next_states[j]
      for nn_s in poss_next_next_states:
        q = Q[next_s,nn_s]
        if q > max_Q:
          max_Q = q
      # Q = [(1-a) * Q]  +  [a * (rt + (g * maxQ))]
      Q[curr_s][next_s] = ((1 - lrn_rate) * Q[curr_s][next_s]) + (lrn_rate * (R[curr_s][next_s] + (gamma * max_Q))) 

      curr_s = next_s
      #loop_control += 1
      
      if curr_s == goal: 
        break
  print('Q2',Q)

# =============================================================
infiniteloop = False
def walk(start, goal, Q):
  global infiniteloop
  loop_control = 0
  curr = start
  print(str(curr) + "->", end="")
  x = -400
  y = -3*10*n
  d[0].draw_outline()
  goto(x,y)
  t.write("0->",font=("Arial", 30, "bold"))
  used_states = []
  while curr != goal:
    if x > 100:
      x = -470
      y -= 30
    x += 70
    next = np.argmax(Q[curr])
    print(str(next) + "->", end="")
    goto(x,y)
    t.write(str(next) + "->",font=("Arial", 30, "bold"))
    
    d[int(next)].fillcolor = 'turquoise'
    d[int(next)].draw_outline()
    used_states.append(curr)
    curr = next
    #d[int(next)].draw()
    #d[int(next)].draw_num()
    loop_control += 1
    if loop_control > n*n or used_states.count(curr) > 9:
      print('...infinity\ninfinite loop - training ended')
      goto(x+70,y)
      t.write("infinite loop - training ended",font=("Arial", 30, "bold"))
      infiniteloop = True
      break
    
  if infiniteloop == False:
    print("done")
    goto(x+70,y)
    t.write("done",font=("Arial", 30, "bold"))

    
  
  
# =============================================================
running = False
def main():
  global running
  if running == False:
    running = True
    np.random.seed(1)
    print("\nSetting up maze in memory")
  
    
    x = 1

    F = np.zeros(shape=[n*n,n*n], dtype=np.int)  # Feasible 
    R = np.zeros(shape=[n*n,n*n], dtype=np.int)  # Rewards
    print('F1 =', F)
    print('R1 =', R)
    for i in range(n):
      for j in range(n-1):
        F[n*j+i,(j+1)*n+i] = x; F[(j+1)*n+i,n*j+i] = x
      for j in range(n-1):
        F[n*i+j,n*i+j+1] = x; F[n*i+j+1,n*i+j] = x
      for j in range(n-1):
        R[n*j+i,(j+1)*n+i] = d[(j+1)*n+i].rwd; R[(j+1)*n+i,n*j+i] = d[n*j+i].rwd
      for j in range(n-1):
        R[n*i+j,n*i+j+1] = d[n*i+j+1].rwd; R[n*i+j+1,n*i+j] = d[n*i+j].rwd
    R[n*n-2,n*n-1] = 10; R[n*n-n,n*n-1] = 10
    print('F2 =', F)
    print('R2 =', R)
    

  # =============================================================

    Q = np.zeros(shape=[n*n,n*n], dtype=np.float32)  # Quality
    
    print("Analyzing maze with RL Q-learning")
    start = 0; goal = n*n-1 #start and end
    ns = n*n  # number of states
    gamma = 0.8
    lrn_rate = 0.5
    max_epochs = 70*n
    train(F, R, Q, gamma, lrn_rate, goal, ns, max_epochs)
    print("Done ")
    
    print("The Q matrix is: \n ")
    my_print(Q)

    walk(start, goal, Q)
screen.onkey(main,'space')  
#if __name__ == "__main__":
#  main()
goto(x+200,y)
#t.write(time.time() - start_time,font=("Arial", 30, "bold"))
print(time.time()-start_time)

screen.listen()
screen.update()
screen.mainloop()
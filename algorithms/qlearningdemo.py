import numpy as np
import random

def my_print(Q):
  rows = len(Q); cols = len(Q[0])
  print("       0      1      2      3      4      5\
      6      7      8      9      10     11\
    12     13     14     ")
  for i in range(rows):
    print(f"{i} ", end="")
    if i < 10: print(" ", end="")
    for j in range(cols): print(" %6.2f" % Q[i,j], end="")
    print("")
  print("")

def get_poss_next_states(s, F, ns):
  # given a state s and a feasibility matrix F
  # get list of possible next states
  poss_next_states = []
  for cs in range(ns):
    if F[s,cs] == 1: poss_next_states.append(cs)
  return poss_next_states

def get_rnd_next_state(s, F, ns):
  # given a state s, pick a feasible next state
  poss_next_states = get_poss_next_states(s, F, ns)
  next_state = random.choice(poss_next_states)
  return next_state 
  #next_state = poss_next_states[np.random.randint(0,len(poss_next_states))]
  
  
  
  

# =============================================================

def train(F, R, Q, gamma, lrn_rate, goal, ns, max_epochs):
  # compute the Q matrix
  for i in range(0,max_epochs):
    curr_s = np.random.randint(0,ns)  # random start state

    movecount = 0
    while(True):
      movecount += 1
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
      
      
      if curr_s == goal: 
        break
  print(Q)

# =============================================================

def walk(start, goal, Q):
  # go to goal from start using Q
  loop_control = 0
  curr = start
  print(str(curr) + "->", end="")
  while curr != goal:
    next = np.argmax(Q[curr])
    print(str(next) + "->", end="")
    curr = next
    loop_control += 1
    if loop_control > 15:
      print('...infinity\ninfinite loop - training ended')
      break
  print("done")

# =============================================================

def main():
  np.random.seed(1)
  print("\nSetting up maze in memory")


  #F = np.zeros(shape=[15,15], dtype=np.int)  # Feasible 
  F = np.array([[0 for x in range(15)] for y in range(15)]) # Feasible 

  F[0,1] = 1; F[0,5] = 1; F[1,0] = 1; F[2,3] = 1; F[3,2] = 1
  F[3,4] = 1; F[3,8] = 1; F[4,3] = 1; F[4,9] = 1; F[5,0] = 1
  F[5,6] = 1; F[5,10] = 1; F[6,5] = 1; F[7,8] = 1; F[7,12] = 1
  F[8,3] = 1; F[8,7] = 1; F[9,4] = 1; F[9,14] = 1; F[10,5] = 1
  F[10,11] = 1; F[11,10] = 1; F[11,12] = 1; F[12,7] = 1
  F[12,11] = 1; F[12,13] = 1; F[13,12] = 1; F[14,14] = 1

  R = np.array([[0 for x in range(15)] for y in range(15)]) # Feasible 
  R[9,14] = 10
  print(F,R)
  if 0 == 1:
    '''
    R = np.zeros(shape=[15,15], dtype=np.int)  # Rewards

    R[0,1] = -0.1; R[0,5] = -0.1; R[1,0] = -0.1; R[2,3] = -0.1
    R[3,2] = -0.1; R[3,4] = -0.1; R[3,8] = -0.1; R[4,3] = -0.1
    R[4,9] = -0.1; R[5,0] = -0.1; R[5,6] = -0.1; R[5,10] = -0.1
    R[6,5] = -0.1; R[7,8] = -0.1; R[7,12] = -0.1; R[8,3] = -0.1
    R[8,7] = -0.1; R[9,4] = -0.1; R[9,14] = 10.0; R[10,5] = -0.1
    R[10,11] = -0.1; R[11,10] = -0.1; R[11,12] = -0.1
    R[12,7] = -0.1; R[12,11] = -0.1; R[12,13] = -0.1
    R[13,12] = -0.1; R[14,14] = -0.1
    '''
 
# =============================================================
  
  Q = np.zeros(shape=[15,15], dtype=np.float32)  # Quality

  print("Analyzing maze with RL Q-learning")
  start = 0; goal = 14 #start and end
  ns = 15  # number of states
  gamma = 0.5
  lrn_rate = 0.5
  max_epochs = 1000
  train(F, R, Q, gamma, lrn_rate, goal, ns, max_epochs)
  print("Done ")
  
  print("The Q matrix is: \n ")
  my_print(Q)

  print("Using Q to go from 0 to goal (3)")

  walk(start, goal, Q)

if __name__ == "__main__":
  main()


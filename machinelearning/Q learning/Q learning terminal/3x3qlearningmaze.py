import numpy as np

# =============================================================


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
  while curr != goal:
    next = np.argmax(Q[curr])
    print(str(next) + "->", end="")
    curr = next
  print("done")

# =============================================================

def main():
  np.random.seed(1)
  print("\nSetting up maze in memory")
 
  x = -0.1
  
  F = np.zeros(shape=[9,9], dtype=np.int)  # Feasible 
  F[0,1] = 1; F[1,0] = 1; F[1,4] = 1; F[4,1] = 1; F[4,5] = 1
  F[5,4] = 1; F[5,2] = 1; F[2,5] = 1; F[4,3] = 1; F[3,4] = 1
  F[3,6] = 1; F[6,3] = 1; F[6,7] = 1; F[7,6] = 1; F[7,8] = 1
  F[8,8] = 1

  R = np.zeros(shape=[9,9], dtype=np.int)  # Rewards
  R[0,1] = x; R[1,0] = x; R[1,4] = x; R[4,1] = x; R[4,5] = x
  R[5,4] = x; R[5,2] = x; R[2,5] = x; R[4,3] = x; R[3,4] = x
  R[3,6] = x; R[6,3] = x; R[6,7] = x; R[7,6] = x; R[7,8] = 10
  R[8,8] = x
  
# =============================================================

  Q = np.zeros(shape=[9,9], dtype=np.float32)  # Quality
  
  print("Analyzing maze with RL Q-learning")
  start = 0; goal = 8 #start and end
  ns = 9  # number of states
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


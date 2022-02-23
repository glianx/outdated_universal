# Rule 30
# left XOR (centre OR right)

# current pattern	            111	110	101	100	011	010	001	000
# new state for center cell	    0	0	0	1	1	1	1	0

import os
import time
os.system('clear')

n = 20
state = [0 for x in range(2*n+1)]
state[n] = 1

next_state = [0 for x in range(len(state))]
state2 = ['⬜️' for x in range(len(state))]

def display():
    state2 = ['🟦' if x else '⬜️' for x in state]
    for x in state2:
        print(x,end = '')
    print()
    time.sleep(0.05)

for i in range(n):
    display()
    for x in range(len(state)-1):
        next_state[x] = int({state[x-1], any([state[x],state[x+1]])} == {0,1})
    state = next_state.copy()
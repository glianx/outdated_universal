import os
import time
import random
os.system('clear')

def render(a):
    os.system('clear')
    for x in li:
        for _ in range(x):
            if x == a: print('🟦',end = '')
            else: print('⬜️',end = '')
        print()
        
    time.sleep(0.05)

def bubblesort(li):
    n = len(li)
    for i in range(n-1):
        for x in range(n-1-i):
            if li[x] > li[x+1]:
                li[x],li[x+1] = li[x+1],li[x]
                render(li[x+1])
                

n = 30
li = [x for x in range(n)]

random.shuffle(li)

start = time.time()

bubblesort(li)

print('runtime:',time.time() - start)
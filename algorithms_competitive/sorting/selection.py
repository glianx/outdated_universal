import os
import time
import random
os.system('clear')

def render(min,current,i):
    os.system('clear')
    for x in li:
        for _ in range(x):
            if x in li[:i]: print('🟨', end = '')
            elif x == min: print('🟥', end = '')
            elif x == current: print('🟦', end = '')
            else: print('⬜️',end = '')
        print()
        
    # time.sleep(0.05)

def selectionsort(li):
    for i in range(len(li)-1):
        min_ = li[i]
        for x in li[i:]:
            if x < min_:
                min_ = x
            render(min_,x,i)
        li.remove(min_)
        li.insert(i,min_)
        


n = 30
li = [x for x in range(n)]

random.shuffle(li)

start = time.time()

selectionsort(li)

runtime = time.time() - start

render(None,None,n)

print('runtime:',runtime)


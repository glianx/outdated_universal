import os
os.system('clear')

def bubblesort(li):
    n = len(li)
    for i in range(n-1):
        for x in range(n-1-i):
            if li[x] > li[x+1]:
                print(li,i,x,li[x],li[x+1])
                li[x],li[x+1] = li[x+1],li[x]


li = [5,4,3,2,1]
print(li)
bubblesort(li)
print(li)

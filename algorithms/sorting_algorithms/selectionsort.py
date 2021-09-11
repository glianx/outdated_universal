import os
os.system('clear')

def selectionsort(li):
    for i in range(len(li)-1):
        min_ = li[i]
        for x in li[i:]:
            if x < min_:
                min_ = x
        li.remove(min_)
        li.insert(i,min_)
        print(li)

li = [2,7,3,5,1,6,4]
print(li)
selectionsort(li)

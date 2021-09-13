li = [0,1,2,3]
li2 = li.copy()

for i in range(4):
    print(li)
    li[i] = li2[i-1]
print(li,li2)



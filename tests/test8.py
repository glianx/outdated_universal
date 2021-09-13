li = [0,1,2,3,4,5,6,7,8,9]
x = 3
li2 = li.copy()
for i in range(x):
    li[i] = li[5:8][i]
    li[-i] = li2[i]
print(li)
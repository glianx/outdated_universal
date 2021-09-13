a,b,c,d,e = 0,1,2,3,4
li = [a,b,c,d,e]
li2 = li.copy()
li2.insert(0,li2.pop(-2))
li2.insert(0,li2.pop(-2))

print(li,li2)

for i in range(5):
    li[i] = li2[i]
print(li,li2)

print(a)
def switch(sc):
    sc[0],sc[1] = sc[1],sc[0]
    print(sc)

def goswitch(c):
    c2 = c.copy()
    switch(c2)
    print(c,c2)

gc = [2,3]
# c2 = gc.copy()

goswitch(gc)
print(gc)
# goswitch(c2)
# print(gc,c2)
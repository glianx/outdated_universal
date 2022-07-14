import string
'''
li = [3, 4, 5]
x, y, z = [i for i in li]
print('x = ',x,y,z)
'''
for x in input():
    for letter in string.ascii_lowercase:
        if x == letter:
            print(string.ascii_lowercase.index(letter))
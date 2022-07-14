import random
import string

'''
def generatepassword(length):
    for m in range(length):
        x = random.SystemRandom().choice(string.ascii_letters + string.digits)
        print(x, end = '')
    print()
generatepassword(6)

def numpassword(length): #random digit
    for m in range(length):
        #print(random.randrange(10),end = '')
        print(random.SystemRandom().choice(string.digits),end = '')
    print()

#numpassword(10)
'''
def numpassword2(length): #random number
    global password
    password = random.randint(10**(length-1),10**length-1)
    print(password)

x = 4
numpassword2(x)

def numpasswordhack(length):
    for x in range(10**(length-1),10**length-1):
        global password
        if x == password:
            print('password found: {}'.format(x))
            
numpasswordhack(x)




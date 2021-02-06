import string

userinput = input("Enter plaintext: ")
slope = int(input('Enter slope: '))
intercept = int(input('Enter intercept: '))
nums = []

for letter in userinput:
    if letter in string.ascii_lowercase:
        print(chr((slope*(ord(letter)-97)+intercept)%26+97),end = '')
        #nums.append((slope*(ord(letter)-97)+intercept)%26)
    elif letter in string.ascii_uppercase:
        print(chr((slope*(ord(letter)-65)+intercept)%26+65),end = '')
        #nums.append((slope*(ord(letter)-97)+intercept)%26)
    else:
        print(letter,end = '')
print()






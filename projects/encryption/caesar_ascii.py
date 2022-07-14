import string
#main
userinput0 = input("enter word: ")
userinput = userinput0.strip()
shift = int(input("enter shift: "))


shift %= 26


for letter in userinput: 
    if 64 < ord(letter) < 91: #capital letter
        if ord(letter) + shift > 90: 
            print(chr(ord(letter) + shift - 26), end = '')
        elif ord(letter) + shift < 65: 
            print(chr(ord(letter) + shift + 26), end = '')
        else: 
            print(chr(ord(letter) + shift), end = '')
    elif 96 < ord(letter) < 123: #lowercase letter
        if ord(letter) + shift > 122: 
            print(chr(ord(letter) + shift - 26), end = '')
        elif ord(letter) + shift < 97: 
            print(chr(ord(letter) + shift + 26), end = '')
        else:
            print(chr(ord(letter) + shift), end = '')
    else: #symbol
        print(letter, end = '')
print('\n')






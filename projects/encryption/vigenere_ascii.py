import string
#main
userinput0 = input("enter word: ")
userinput = userinput0.strip()

userinputkey0 = input("enter keyword: ")
userinputkey = userinputkey0.strip()

shifts = [] #distance of letters in key from 'a'


ltrcount = 0

for letter in userinputkey: #adds distance of letters to shifts[]
    shifts.append(ord(letter)-97)
    ltrcount = ltrcount + 1

print("shift",userinputkey,"=",shifts)

position = 0 

for letter in userinput: 
    #print(position,chr(ord(letter)))
    
    if 64 < ord(letter) < 91: #capital letter
        if ord(letter) + shifts[position%ltrcount] > 90:
            print((chr(ord(letter) + shifts[position%ltrcount] - 26)), end = '')
        else:
            print((chr(ord(letter) + shifts[position%ltrcount])), end = '') 

    elif 96 < ord(letter) < 123: #lowercase letter
        if ord(letter) + shifts[position%ltrcount] > 122:
            print((chr(ord(letter) + shifts[position%ltrcount] - 26)), end = '')
        else:
            print((chr(ord(letter) + shifts[position%ltrcount])), end = '')
    
    else: #symbol
        print(chr(ord(letter)), end = '')
        position = position - 1
    position = position + 1
print('\n')



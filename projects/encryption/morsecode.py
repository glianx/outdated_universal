import string
morsecode = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 
'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 
'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 
'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 
'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', 
'4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', 
'0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', 
'(':'-.--.', ')':'-.--.-'} 

encryption_morsecode = ''

for letter in input('Enter message: ').upper():
    try:
        if letter == ' ':
            encryption_morsecode += (' / ')
        elif letter:
            encryption_morsecode += morsecode[letter] + ' ' 
    except:
        encryption_morsecode += letter + ' ' 
print(encryption_morsecode)   
print()



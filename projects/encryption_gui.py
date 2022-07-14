from tkinter import * 
import tkinter as tk
from tkinter import Tk, Label
from tkinter import Text, Tk
import string
window = Tk()
window.geometry('1600x600')

def encrypt_caesar():

    userinput = userinput0.get().strip()
    encryption_caesar = ''
    if TypeError:
        ciphertext.configure(text = 'error: not int')
        ciphertext.place(x = 1000, y = 50)
    
    shift = int(userinput1.get())
    shift %= 26

    for letter in userinput: 
        if letter in string.ascii_uppercase: #capital letter
            if ord(letter) + shift > 90: 
                encryption_caesar += (chr(ord(letter) + shift - 26))
            elif ord(letter) + shift < 65: 
                encryption_caesar += (chr(ord(letter) + shift + 26))
            else: 
                encryption_caesar += (chr(ord(letter) + shift))
        elif letter in string.ascii_lowercase: #lowercase letter
            if ord(letter) + shift > 122: 
                encryption_caesar += (chr(ord(letter) + shift - 26))
            elif ord(letter) + shift < 97: 
                encryption_caesar += (chr(ord(letter) + shift + 26))
            else:
                encryption_caesar += (chr(ord(letter) + shift))
        else: #symbol
            encryption_caesar += (letter)
    ciphertext.configure(text = encryption_caesar)
    ciphertext.place(x = 1000, y = 50)




def encrypt_vigenere():
    userinput = userinput0.get().strip()
    userinputkey = userinput1.get().strip()
    shifts = [] #distance of letters in key from 'a'
    encryption_vigenere = ''

    ltrcount = 0 #number of letters in userinputkey

    for letter in userinputkey: #adds distance of letters to shifts[]
        if letter not in string.ascii_letters:
            ciphertext.configure(text = 'error: invalid key')
            ciphertext.place(x = 1000, y = 50)
            break
        shifts.append(ord(letter)-97)
        ltrcount = ltrcount + 1

    position = 0 

    for letter in userinput: 
        
        if letter in string.ascii_uppercase: #capital letter
            if ord(letter) + shifts[position%ltrcount] > 90:
                encryption_vigenere += chr(ord(letter) + shifts[position%ltrcount] - 26)
            else:
                encryption_vigenere += chr(ord(letter) + shifts[position%ltrcount])

        elif letter in string.ascii_lowercase: #lowercase letter
            if ord(letter) + shifts[position%ltrcount] > 122:
                encryption_vigenere += chr(ord(letter) + shifts[position%ltrcount] - 26)
            else:
                encryption_vigenere += chr(ord(letter) + shifts[position%ltrcount])
        
        else: #symbol
            encryption_vigenere += chr(ord(letter))
            position = position - 1
        position = position + 1

    ciphertext.configure(text = encryption_vigenere)
    ciphertext.place(x = 1000, y = 50)

def newEntry():
    #text3 = Label(window,font = ("Arial",40), text = "Int:", bg = "white", fg = "black")
    #text3.place(x=750, y=5)
    pass
    #userinput2.place(x=750, y=50)

def encrypt_affine():
    userinput = userinput0.get().strip()
    slope,intercept = userinput1.get().split(',')
    #intercept = int(userinput2.get())
    slope,intercept = int(slope),int(intercept)
    print(slope,intercept)
    encryption_affine = ''

    if slope%2 == 0:
        ciphertext.configure(text = 'error: key cannot be even')
        ciphertext.place(x = 1000, y = 50)
    else:
        for letter in userinput:
            if letter in string.ascii_lowercase:
                encryption_affine += chr((slope*(ord(letter)-97)+intercept)%26+97)
            elif letter in string.ascii_uppercase:
                encryption_affine += chr((slope*(ord(letter)-65)+intercept)%26+65)
            else:
                encryption_affine += letter
        ciphertext.configure(text = encryption_affine)
        ciphertext.place(x = 1000, y = 50)

def encrypt_morse():
    morsecode = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 
    'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 
    'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 
    'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 
    'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', 
    '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', 
    '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', 
    '(':'-.--.', ')':'-.--.-'} 

    encryption_morsecode = ''

    for letter in userinput0.get().strip().upper():
        try:
            if letter == ' ':
                encryption_morsecode += (' / ')
            elif letter:
                encryption_morsecode += morsecode[letter] + ' ' 
        except:
            encryption_morsecode += letter + ' ' 
    ciphertext.configure(text = encryption_morsecode)
    ciphertext.place(x = 1000, y = 50)
    print()

def testText():
    pass



cipher_options = ["caesar","affine","vigenere","morsecode"]

variable = StringVar(window)
variable.set(cipher_options[0]) # default value

dropdown = OptionMenu(window, variable, * cipher_options)
dropdown.place(x = 500, y = 50)


def encrypt():
    global affineflag
    if variable.get() == cipher_options[0]:
        encrypt_caesar()
    elif variable.get() == "affine":
        encrypt_affine()
    elif variable.get() == cipher_options[2]:
        encrypt_vigenere()
    elif variable.get() == cipher_options[3]:
        encrypt_morse()


text = Label(window,font = ("Arial",40), text = "Plaintext:", bg = "white", fg = "black")
userinput0 = Entry(window,font = ("Arial",40),width = 19, bg = "white", fg = "steelblue")
btn = Button(window, text = "Encrypt",width = 40,font = ("Arial", 50), command = encrypt,bg = "steelblue", fg = "orangered")
text1 = Label(window,font = ("Arial",40), text = "Key:", bg = "white", fg = "black")
userinput1 = Entry(window,font = ("Arial",40),width = 4, bg = "white", fg = "steelblue")
#userinput2 = Entry(window,font = ("Arial",40),width = 4, bg = "white", fg = "steelblue")
ciphertext = Label(window, text= '', font = ("Arial", 40), fg = "steelblue",width = 25, bg = "white", anchor="w", justify=LEFT)
text2 = Label(window,font = ("Arial",40), text = "Ciphertext:", bg = "white", fg = "black",borderwidth = 2,highlightthickness=4, highlightbackground="#37d3ff")

var = tk.StringVar()
l = tk.Label(window, bg='white', width=20, text='empty')

#rbtn1 = tk.Radiobutton(window, text='Caesar', variable=var, value='A', command=encrypt_caesar)
#rbtn2 = tk.Radiobutton(window, text='Vigenere', variable=var, value='B', command=encrypt_vigenere)
#rbtn3 = tk.Radiobutton(window, text='Affine', variable=var, value='C', command=newEntry)

text.grid(column = 0,row = 0)
userinput0.grid(column = 0,row = 1)
btn.place(x=5, y=150)

#rbtn1.place(x = 500, y = 50)
#rbtn2.place(x = 500, y = 80)
#rbtn3.place(x = 500, y = 110)

text1.place(x=600, y=5)
userinput1.place(x=600, y=50)

text2.place(x=1000, y=0)



#entry4 = Text(window, height=5, width=19, font = ("Arial",40), bg = "white", fg = "steelblue",bd = 20)
#entry4.place(x=20,y=60)
window.mainloop()
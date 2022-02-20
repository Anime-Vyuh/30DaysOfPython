Program 4: Moorse Code

Here let us create two Python file. In one .py file store the Moorse Code. And In other .py file write a code to convert Text to Moorse Code


import string

alpha = string.ascii_uppercase
mc=['.-','-...','-.-.','-...','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
moorse = dict()
for code in range(len(alpha)):
    moorse[alpha[code]]=mc[code]


text = input("Enter the Text: ").upper()
with open("Before.txt","w") as file:
    file.write(text)
file.close()

#double space means new letter, while single space is gap between two moose converted letter
moorse_converted = ""
for letter in text:
    if letter==" ":
        moorse_converted+="  "
    if letter in moorse:
        moorse_converted+=moorse[letter]+" "

with open("After.txt","w") as new:
    new.write(moorse_converted)

new.close()
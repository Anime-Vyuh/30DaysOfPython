"""
Moorse Code: A-Z alphabets is replaced with sequence of dits(.) and dahs(-)

Here let us create two Python file. In one .py file store the Moorse Code. And In other .py file write a code to convert Text to Moorse Code

"""
import string

alpha = string.ascii_uppercase
mc=['.-','-...','-.-.','-...','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
moorse = dict()
for code in range(len(alpha)):
    moorse[alpha[code]]=mc[code]
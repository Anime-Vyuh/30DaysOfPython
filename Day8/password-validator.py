import string
import time

def login():
    username=input('Enter your name:')
    password=input('Enter the password:')
    return password

def passdetails():
    print('*'*35)
    print('The password must contain total of 14 charachters')
    print('It must contain one upper case with total of minimum 8 letters')
    print('it must contain 2 numbers')
    print('It must contain atleast one special character')
    print('*'*35)

def passtype(pword):
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    number=string.digits
    symbol=string.punctuation
    lower_count=upper_count=number_count=symbol_count=0
    for letter in pword:
        if letter in lower:
            lower_count+=1
        if letter in upper:
            upper_count+=1
        if letter in number:
            number_count+=1
        if letter in symbol:
            symbol_count+=1
    if(lower_count>=7 and upper_count>=1 and number_count>=2 and symbol_count>=1):
        return('Strong')
    else:
        return('Weak')

passdetails()
time.sleep(5)
password=login()
print(passtype(password))
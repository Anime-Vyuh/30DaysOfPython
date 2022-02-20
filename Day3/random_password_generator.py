import random
import string

def satisfied():
    while True:
        response=input('Are you Satisfied?(Y/n)').lower()
        if response[0] not in ['y','n']:
            print("***Invalid entry(enter y/n)***")
            continue
        if response.startswith('y'):
            return True
        else:
            return False

def main():
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    numbers=string.digits
    symbols = string.punctuation
    password = []
    for _ in range(2):
        password.append(random.choice(upper_case)+random.choice(numbers)+random.choice(symbols))
    for _ in range(8):
        password.append(random.choice(lower_case))
    print(''.join(password))
    if satisfied():
        print("Your Password is:{}".format(''.join(password)))
        print("Thank You")
    else:
        main()

main()


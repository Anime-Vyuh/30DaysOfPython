phonebook = dict()

def is_valid(number,name):
    # check for valid name and number
    # observe we have used if else in single statement
    # number should be exactly 10 digit & name should be >3 letters
    response = True if len(number)==10 and number.isdigit() and len(name)>=3 else False
    return response

def keep_searching():
    while True:
        #ask user if he wants to continue or quit
        move = input("Do you want to continue(c) or quit(q)?").lower()
        if move not in ['c','q']:   #if user enters other than c or q
            print("Enter c to continue or q to quit: ")
            continue
        else:
            if move.startswith('c'):
                return True
            return False

while True:
    name = input("Enter your name:").lower()
    phone_number = input("Enter your number:")
    if is_valid(phone_number,name):
        phonebook[name]=phone_number
    else:
        print("Invalid Entry..")
        continue

    print("Look Into PhoneBook")
    search_name = input("Search the name in the Phonebook: ").lower()
    if search_name in phonebook:
        print(search_name,"number is",phonebook[search_name])
    else:
        avaiable = input("Name and number not stored, Do you want add it?(Y/n):").lower()
        if avaiable.startswith('y'):
            new_number = input("Enter the number to be stored: ")
            if is_valid(new_number,search_name):
                phone_number[search_name]=new_number
            else:
                print("Failed to Update")

    if keep_searching():
        continue
    else:
        print("Thank you for visiting..")
        break
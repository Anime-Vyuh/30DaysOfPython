"""
Suppose you want your program to run error free, well everyone wants that.
But what if we need our program to run even if there is an error, is there any possibility? Yes There sure is.
Python provides Try and except, using this you can show user the message when certain error is occurred we call it exception.
User get the feedback where he went wrong, using Try And Except Technique.
Giving feedback for your program is every important.
I hope even I do get some feedback about this 30DaysOfPython, I will be waiting for your feedback.
Back to Try and Except again, here you will require the knowledge of some common errors
"""
#example 1

try:
    a = int(input("Enter a number: "))   #integer inputs required
    b = int(input("Enter a number2: "))
    div = a/b
    if a>b:
        print("{} is greater than {}. Quotient is:{}".format(a,b,div))
    else:
        print("{} is greater than {}. Quotient is:{}".format(b,a,div))

except ValueError as e:
    #this except block is printed when user enters a string instead of integer
    print("This Occured:",e)
except ZeroDivisionError as e:
    #this except block is printed when user inputs 0 to number 2, b
    print("This occured:",e)

#example 2
try:
    ceo = {"Google":"Sundar Pichai",
    "Microsoft":"Satya Nadella",
    "Adobe":"Shantanu Narayen",
    "Tesla":"Elon Musk",
    "Apple":"Tim Cook",
    "Facebook":"Mark Zuckerberg"}

    ceo['Amazon'] = "Andy Jassy"

    print(ceo["PayTM"])
    print(ceo["Google"])
    print(ceo["Tesla"])
    print(ceo["Amazon"])
    print(ceo["Apple"])

except KeyError as k:
    #this except block is executed when invalid key is entered
    print("This key is not found in the dictionary",k)
except Exception as e:
    print("Something went wrong",e)

#example 3

try:
    with open("unknownfile.txt") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Oops! No File Found, Check Folder of the file and Try Again:)")

# Try and Except

We know of errors now. Suppose you want your program to run error free, well of course everyone wants that. But you need your program to run even if there is error, is there any possibility? Yes There is. Python provides `Try and except`, using this you can show user the message when certain error is occurred, so user get the feedback where he went wrong. Giving feedback for your program is every
important. I hope even I do get some feedback about this repo, I will be waiting for your feedback. Back to `Try and Except` again, here you will require the knowledge of Error, that’s the reason why we covered about Error before starting it.

```py
manga = "Vagabond"
try:
    print(manhwa)
except:
    print("Name Error occurred")

Name Error occurred

try:
    print(manhwa)
except NameError as error:
    print("This is what happened:",error)
```

This is what happened: name `manhwa` is not defined. Now, suppose you have declared a variable of name x and print y, you will get into `NameError`. What try and except does here is, you will execute your code inside try block and if in case you run into some error

```py
try:
    print(manga)
except:
    print("This is what happened:",error)

Vagabond
```

```py
number = 100
episode = 24
try:
    print(episode-4)
    print(episode/0)
except ZeroDivisionError as error:
    print("This happened:",error)
Output:
20
This happened: division by zero
```

We have added error name `ZeroDivisionError` in except block, if you don’t know what error you are dealing with then you can mention except Exception as e and
deal with the problem.

## Finally

Finally is a add-on option that comes handy with try and except.

```py
try:
    print(episode/0)
except ZeroDivisionError as error:
    print("This happened:",error)
finally:
    print("We have reached the end of code")

Output:
This happened: division by zero
We have reached the end of code

try:
    pass
except:
    print("Somethings not Good")
finally:
    print("I will be executed no matter what")

Output:
I will be executed no matter what
```

Lets look at some programs where we can put `try and except` in amazing use.

```py
try:
    a = int(input("Enter a number: ")) #integer inputs required
    b = int(input("Enter a number2: "))
    div = a/b
    if a>b:
        print("{} is greater than {}. Quotient is:{}".format(a,b,div))
    else:
        print("{} is greater than {}. Quotient is:{}".format(b,a,div))
except ValueError as e:
    print("This Occured:",e)
except ZeroDivisionError as e:
    print("This occured:",e)

Output for different input cases:
Enter a number: 10
Enter a number2: 5
10 is greater than 5. Quotient is:2.0
Enter a number: 5
Enter a number2: 10
10 is greater than 5. Quotient is:0.5
Enter a number: p
This Occured: invalid literal for int() with base 10: 'p'
Enter a number: 10
Enter a number2: 0This occured: division by zero
Enter a number: 0
Enter a number2: p
This Occured: invalid literal for int() with base 10: 'p'
```

Example 2,

In Dictionary we had taken the example of CEO, lets consider that example again but with try and except method.

```py
ceo = {
    "Google":"Sundar Pichai", "Microsoft":"Satya Nadella",
    "Adobe":"Shantanu Narayen","Tesla":"Elon Musk",
    "Apple":"Tim Cook","Facebook":"Mark Zuckerberg"}
print(ceo["Google"])
print(ceo["Tesla"])
print(ceo["Amazon"])
print(ceo["Apple"])

Output:
Sundar Pichai
Elon Musk
KeyError: 'Amazon'
```

We get a `KeyError` because we haven’t declared Amazon name yet. Now add a new
key entry for Amazon and also add `Try and Except` method so that user gets the feedback on what he should do if he gets into some error.

```py
try:
ceo = {"Google":"Sundar Pichai",
"Microsoft":"Satya Nadella",
"Adobe":"Shantanu Narayen",
"Tesla":"Elon Musk",
"Apple":"Tim Cook",
"Facebook":"Mark Zuckerberg"}
ceo['Amazon'] = "Andy Jassy"
print(ceo["PayTM"])print(ceo["Google"])
print(ceo["Tesla"])
print(ceo["Amazon"])
print(ceo["Apple"])
except KeyError as k:
print("This key is not found in the dictionary",k)
except Exception as e:
print("Something went wrong",e)
Output:
This key is not found in the dictionary 'PayTM'
```

`Try and except` is the best way to deal with error. And with this you can generate your own message every time you run into error, this enables you to understand the code in better way.

## How To Deal With FileNotFoundError?

We discussed about `FileNotFoundError` while discussing [files]( https://animevyuh.org/files-in-python/), and we will deal with it using `Exception Handling`. This is no big task to you, isn’t? You are supposed to follow the same steps we followed in rest of the Exception handling programs.

```py
try:
    with open("unknownfile.txt") as file:
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Oops! No File Found, Check Folder of the file and Try Again:)")
Output:
Oops! No File Found, Check Folder of the file and Try Again:)
```

We have a good error message for displaying File not Found.

### Raise Exception

So far in try and except, whenever we encountered an error a normal message was
executed. But what if you need to generate an error in addition with a meaning
message. `raise` keyword does that job by returning an error with the message we
provide in except block.

```py
try:
    a = int(input("Enter the a value:"))
    b = int(input('Enter the b value:'))
    result = a/b
    print(result)
except ValueError:
    #first method to raise an exception by mentioning error name in except :
    raise "Enter a valid number"
except:
    #second method to raise an exception without mentioning name in except:
    raise ZeroDivisionError("Enter non zero number for b")

Output:
Enter the a value:a
Traceback (most recent call last):
File "/home/pythonbook/s.py", line 2, in <module>
a = int(input("Enter the a value:"))
ValueError: invalid literal for int() with base 10: 'a'
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
File "/home/pythonbook/s.py", line 7, in <module>
raise "Enter a valid number"
TypeError: exceptions must derive from BaseException

Enter the a value:2
Enter the b value:0
Traceback (most recent call last):
File "/home/pythonbook/s.py", line 11, in <module>
raise ZeroDivisionError("Enter non zero number for b")
ZeroDivisionError: Enter non zero number for b
```

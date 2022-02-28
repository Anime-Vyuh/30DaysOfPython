We can check for exception using Try and Except method. But before that in the beginning of the book I had said that I will explain SyntaxError and other Errors in detail, Here are the major Error which we encounter very often:
1. SyntaxError
2. NameError
3. ValueError
4. TypeError
5. IndexError

### 1. SyntaxError

You get syntax SyntaxError when you don’t follow rules and regulations provided by
Python. Major exampled missing of parenthesis, missing of clone, Invalid naming of
variable, Spelling mistake for the keywords and many more.

Examples of SyntaxError:

```py
>>> 10 = 32
SyntaxError: cannot assign to literal
>>> print "Very good"
SyntaxError: Missing parentheses in call to 'print'.
>>>if (a>b) #missing colon
File "<stdin>", line 1
if (a>b)
^
SyntaxError: invalid syntax
>>> ife(20>10):
SyntaxError: invalid syntax
```

### 2. NameError

You get NameError when you try to use a variable or a function name that is not
valid. This means that if Python encounters a name that it doesn’t recognize, you’ll
probably get this error. Some common causes are: Misspelling the name of a build-in function, Forgetting to give a value to a variable before using it in a different
statement.

Examples of NameError:

```py
>>>x+=1
NameError: name 'x' is not defined
>>>name=(manhwa)
NameError: name 'manhwa' is not defined
>>>print(hello)
NameError: name 'hello' is not defined
>>> prin("Python is easy to learn")
NameError: name 'prin' is not defined
```

### 3. Value Error

You get ValueError when a value is not the expected type.

Examples of ValueError:

```py
>>> x=int("Can you write a Python Program")
ValueError: invalid literal for int() with base 10: 'what about this statement'
>>> z=[1,3,5,7,9]
>>> x,y = z
>>> print(x)
>>> print(y)
ValueError: too many values to unpack (expected 2)
>>>points=float(“int”)
ValueError: could not convert string to float: 'int'
```

### 4. Type Error

You get TypeError when an operation is performed on an inappropriate object type.

Examples of TypeError:

```py
>>>a=input(‘Enter a number:’)
>>>b=a+10
… print(“10 more is {}”.format(y))
TypeError: can only concatenate str (not "int") to str
>>>x=5
>>>y=”123”
… print(x+y)TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

### 5. Index Error

You get IndexError when your code try to access an Index value that is not valid. This
usually happen because the index out of bonds due to being too large.

Examples of IndexError:

```py
>>>s=[1,2,4,6,8}
>>>print(s[5])
IndexError: list index out of range
>>>name=[“Itachi”, “Naruto”, “Madara”, “Sasuke”, “Luffy”]
>>>name.pop(6)
… print(name)
IndexError: pop index out of range
```
"""
Program 5: Strong or Weak password
Let a user enter a password you just have to print Strong or weak, and nothing
else.
A password is said to be strong:
 If password should at-least be 8 letters long
 Password must contain at least one upper case characters [A-Z]
 Password must contain at least 2 numbers [0-9]
 Password must contain at least one 1 special symbol [.,%$#@!^&*():"]
If the above criteria as meet then print Strong, else Weak.
Sample Input: password?!123
Sample Output: Weak [because no upper case character]
Sample Input: LuffyKing&100
Sample Output: Strong
"""
import string
import sys
password = input("Enter your password:")
if len(password)<8:
    print("Weak")
    sys.exit()

numbers,upper_case,symbol = 0,0,0
for check in password:
    if check in string.ascii_uppercase:
        upper_case+=1
    elif check in string.punctuation:
        symbol+=1
    elif check in string.digits:
        numbers+=1
    else:
        pass

if upper_case>=1 and numbers>=2 and symbol>=1:
    print("Strong")
else:
    print("Weak")
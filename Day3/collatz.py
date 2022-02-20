""""
Write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1. (Amazingly enough, this sequence actually works for any integer sooner or later, using this sequence, you'll arrive at 1! Even mathematicians aren't sure why. Your program is exploring what's called the Collatz sequence, sometimes called the simplest impossible math problem.) Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a string value. Hint: An integer number is even if number % 2 == 0, and it's odd if  number % 2 == 1. The output of this program could look something like this:

Sample input: 3
Sample output:
10
5
16
8
4
2
1

Sample input: 5
Sample output:
16
8
4
2
1
"""
def collatz(number):
  try:
    num=int(input(number))
    while num>1:
      if num%2==0:
        num=k=num//2
        print(k)
      else:
        num=g=num*3+1
        print(g)
  except ValueError:
    print('Number should be integer and not string')

collatz('Enter a number:')
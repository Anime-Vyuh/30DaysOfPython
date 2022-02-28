For Tutorials: [Check Anime Vyuh](https://animevyuh.org/category/python-tutorials

### Program 1:

Write a Program to swap data between two variables

Open your Interactive shell or text editor or IDE anything you are comfortable with it

Method 1 to swap with temp

```py
main_character = "Light yagami"
loved_character = "L Lawleit"
print(‘Before Swap:’)
print(‘Main Character:’,main_character)  #light is output
print(‘Side Character:’,loved_character)      #l is output
temp = main_character                      #create a temporary variable to store main variable in it
main_character = loved_character  #loved_character name Is successfully swaped to main
loved_character = temp                      #temp which had main in it is swaped to loved
print(‘After Swap:’)
print(‘Main Character:’,main_character)  #l is output
print(‘Side Character:’,loved_character) #light is output
```

Results are swapped, run the program to see changes.

Method 2 to swap without temp

```py
main_character = "Light yagami"
loved_character = "L Lawleit"
print(‘Before Swap:’)
print(‘Main Character:’,main_character)  #light is output
print(‘Side Character:’,loved_character)      #l is output 
main_character,loved_character = loved_character,main_character   #swap successful
print(‘After Swap:’)
print(‘Main Character:’,main_character)  #l is output
print(‘Side Character:’,loved_character) #light is output
```

### Program 2:

Write a Program to convert Dollar to Rupee and add 50 rupee as tip

```py
dollar = 56.76
dollar_to_INR = 77.76
rupee = dollar * dollar_to_INR
final_amt = rupee + 50.00
print(final_amt)
```

### Program 3:

You are the owner of restaurant greet your customer with specific inputs
[user input includes name and dish he could like to eat]

```py
name = input("Enter Customer Name:")
dish = input("What could you like to it? ")
print("Welcome to Anime Foods "+name) #you can also use comma, instead of +
print("We could love to serve "+dish)
print("Thank you for coming")
```

### Program 4

Take two input numbers and perform addition, subtraction, multiplication and division

```py
num1 = int(input("Enter num1: ")) #ask for integer input
num2 = int(input("Enter num2: "))
add = num1+num2
sub = num1-num2
mul = num1*num2
divide = num1/num2
print("Sum =",add)
print("Difference =",sub)
print("Multiply =",mul)
print("Division =",divide)
```

### Program 5

Write a program for a conversation between two people. [USE: input()]

```py
person1 = input("Enter Person1 name:")
person2 = input("Enter Person2 name:")
print(person2,":Hello",person1)
print(person1,":Nice to meet you",person2)
print(person2,":Can I know your age?")
age_person1 = int(input())
age_person2 = int(input())
print(person1,":I am",age_person1,"years old, May I know your age?")
print(person2,":I am",age_person2)
```

Check [Anime Vyuh](https://animevyuh.org/) For more
Follow on [Twitter](https://twitter.com/TRJ_0751)

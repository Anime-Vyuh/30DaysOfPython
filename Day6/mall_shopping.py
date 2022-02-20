"""
Imagine your in a Mall for Shopping, you come across a store that serves good food. The Menu is displayed to you, you decide the food you like and add it in cart. Once you decided your meal, you now need to order and pay the amount for you meal. And at end display a Thank You message.
"""
import termcolor
def display_menu():
    menu = {
        "Papad Salad":60,
        "Manchurian Soup":100,
        "Jalebi And Fafda":150,
        "Baby-Corn Machuri":85,
        "Paneer Tikka":100,
        "Hamburger":120,
        "Double Cheese Decker Pizza":199,
        "Butter Kulcha":45,
        "Roti":30,
        "Malai Kofta":100,
        "Dal Fry":80,
        "Fried Rice":140,
        "Death By Chocolate Desert":200,
        "Hot Chocolate":180
        }

    termcolor.cprint("\n\t****Welcome To Anime Vyuh Foods****\t\n",color="red")
    termcolor.cprint("\n\tHere is the Menu:\n\n",color="yellow")
    for food,price in menu.items():
        termcolor.cprint("{} {} :{}INR".format(food,''*20,price),"blue")

    return menu

course_menu = display_menu()
cart = []
print("What could you like to eat? Enter the name from the menu")
while True:
    eat = input("\nAdd Food Name?(q to quit):")
    if eat.lower().startswith('q'):
        break
    if eat not in course_menu.keys():
        print("Invalid Entry! Check the Spelling and Try again:")
    else:
        print(eat,"added to eat list.")
        cart.append(eat)

print("The Amount To Be Paid:",end="")
amt = 0
for i in cart:
    amt=amt+course_menu[i]

print(" {} INR\n".format(float(amt)))
print("Thank You For Visiting Us")
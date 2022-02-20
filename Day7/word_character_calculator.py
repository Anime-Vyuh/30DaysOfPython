"""
Character and Word Calculator
Write a program to print total words, total characters including spaces and total characters excluding characters from the reference.txt.

reference.txt :

Anime Quotes of Main Characters:
Naruto: "Until I become Hokage, I can't die"
Luffy: "I will become the Pirate King, I dont care if I die trying"
Hinata: "Do you need a reason to win?"
Gintoki: "The night is dark before dawn, But don't close your eyes"
"""
with open("reference.txt") as ref_file:
    content = ref_file.read()

space,without_space=0,0
for word in content:
    if word == "\n":
        pass
    elif word == ' ':
        without_space+=1
    else:
        without_space+=1
        space+=1

print(" Total Words:{} \n Total Characters:{} \n Total Characters without space:{}".format(len(content.split()),without_space,space))
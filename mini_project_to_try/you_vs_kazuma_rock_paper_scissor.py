import random

def play(rock_paper_scissor):
    while True:
        player_choice=input('Enter Rock/Paper/Scissors: ').capitalize()
        if player_choice not in rock_paper_scissor:
            continue
        else:
            return player_choice

def winner(player_choice,kazuma_choice,kazuma_score,player_score):
    if player_choice==kazuma_choice:
        print('Draw')   #the winner is rewarded by 2 points but on draw both player and kazuma gets 1 point
        kazuma_score+=1
        player_score+=1
        print(f'Player Choice:{player_choice} || Kazuma Choice:{kazuma_choice}')
        print(f'Player score:{player_score} || Kazuma score:{kazuma_score}')
    elif (player_choice=='Rock' and kazuma_choice=='Paper') or (player_choice=='Paper' and kazuma_choice=='Scissor') or (player_choice=='Scissor' and kazuma_choice=='Rock'):
        print(f'Kazuma won')
        player_score+=0
        kazuma_score+=2
        print(f'Player Choice:{player_choice} || kazuma Choice:{kazuma_choice}')
        print(f'Player score:{player_score} || kazuma score:{kazuma_score}')
    elif (player_choice=='Rock' and kazuma_choice=='Scissor') or (player_choice=='Scissor' and kazuma_choice=='Paper') or (player_choice=='Paper' and kazuma_choice=='Rock'):
        print(f'Player won')
        player_score+=2
        kazuma_score+=0
        print(f'Player Choice:{player_choice} || kazuma Choice:{kazuma_choice}')
        print(f'Player score:{player_score} || kazuma score:{kazuma_score}')
    else:
        print('Invalid')

def permission():
    ask=input('Are you ready?(Y/n)').lower()
    if ask.startswith('y'):
        return True
    else:
        return False

def play_again():
    print('*'*30)
    again=input('Do you want to play again?(Y/n)').lower()
    print('*'*30)
    if again.startswith('y'):
        return True
    else:
        print('Thank You for playing')

choice=['Rock','Paper','Scissor']
player=input('Enter Your Name:')
ps=cs=0
kazuma_choice=random.choice(choice)
if permission():
    player_choice=play(choice)
    winner(player_choice,kazuma_choice,cs,ps)
    while play_again():
        kazuma_choice=random.choice(choice)
        player_choice=play(choice)
        winner(player_choice,kazuma_choice,cs,ps)
else:
    print("Thank You for playing")
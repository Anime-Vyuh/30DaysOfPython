import random
import time

def game_rules():
    rules = """
    Rules: A simple 2 player game [Bungou Stray Dogs Season 3 Episode 4]
    1. Inially open one card, i.e., display one card from shuffled deck
    2. Now player1 takes a card from the deck
    3. Now it begins, the other player:[player2] should guess if the taken card is higher or lower from than the previous card
    **[ say the first card is 9, now one player should guess if the next card is high or low
    i.e., if 1-8 appears it is low, 10-12 and A appears then it is high
    now player1 reveals the next card, say it is 10.
    Now 10 is the previous card, now guess high or low based on number 10.
    ]**
    4. If the player2 guessed correctly then player1 is again suppose to take another card
    5. Now when player2 guessed correctly, that drawn card is added in player1 penalty.
    6. If the player2 guess is wrong, then player2 will take the card and player1 will guess
    7. Since player2 guessed wrong, that card will be counted as player2 penalty.
    8. The game continues till all 51 cards are revealed [1 card will be opened in beginning so 51]
    9. At end who as more penalty cards loses, and player with less penalty cards win.
    ***********
    10. Penalty card calculation:
    if player1 guessed wrong, player1 gets penalty, now player2 have to guess
    if player1 guessed correctly, player2 gets penalty, since guess is correct player1 itself should guess again
    ***********
    """
    return rules

def deck_52_cards():
    deck = list()
    deck.clear()
    suits = ['H','S','D','C']  #Hearts, Spades, Diamond, Club
    for suit in suits:
        for card in range(1,14):
            deck.append(suit+str(card))
    random.shuffle(deck)
    return deck

def winner(guess_cards,p1_name,p2_name):
    base=first_card = random.choice(guess_cards)
    print("First Card:",first_card)
    guess_cards.remove(first_card)
    player1_penalty_scores,player2_penalty_scores = 0,0
    turn = p2_name
    no_turn = p1_name

    while True:
        if len(guess_cards)==0:
            print("\n\t Match Over \n")
            break

        guess=input("{} guess High or Low:".format(turn)).lower()
        if guess not in ['high','low']:
            continue

        next_card = random.choice(guess_cards)
        guess_cards.remove(next_card)
        print("Previous card:",base)
        print("New Card:",next_card)

        correct = "low" if(int(base[1:])>int(next_card[1:])) else "high"  #correct is low for True if condition else correct=High
        if guess==correct:
            print("{} Correct {}".format('*'*10,'*'*10))
            if turn==p1_name:
                player2_penalty_scores+=1
            else:
                player1_penalty_scores+=1
        else:
            print("{} Wrong, Next {}".format('*'*10,'*'*10))
            if turn==p2_name:
                turn=p1_name
                player2_penalty_scores+=1
            else:
                turn=p2_name
                player1_penalty_scores+=1

        base=next_card

    return(p1_name if(player2_penalty_scores>player1_penalty_scores) else p2_name)

def play_again():
    ask = input("Do you want to play again(Y/n)? ").lower()
    if ask.startswith('y'):
        main()
        return True
    print("Thank You ")

def main():
    #guess high or low
    game_details = input("Do you want to see the rules(Y/n)? ").lower()
    if game_details.startswith('y'):
        print(game_rules())
        time.sleep(15)
        print("Game will start in 5 seconds .....")
        time.sleep(5)

    print("\n\n\t Let the Game Begin \n\n")
    cards = deck_52_cards()
    player1 = input("Player 1 enter your name: ")
    player2 = input("Player 2 enter your name: ")
    winner_of_the_game = winner(cards,player1,player2)
    print("Winner is",winner_of_the_game)
    play_again()

if __name__ == '__main__':
    main()
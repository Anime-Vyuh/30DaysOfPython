import random
import string

hangman_body = ['''
                ------
                    |
                    |
                    |
                    |
                ========''','''
                ------
                |   |
                    |
                    |
                    |
                ========''' ,'''
                ------
                |   |
                o   |
                    |
                    |
                ========''','''
                ------
                |   |
                o   |
                |   |
                    |
                ========''','''
                ------
                |   |
                o   |
               /|   |
                    |
                ========''','''
                ------
                |   |
                o   |
               /|\  |
                    |
                ========''','''
                ------
                |   |
                o   |
               /|\  |
               /    |
                ========''','''
                ------
                |   |
                o   |
               /|\  |
               / \  |
                ========''',
             ]
def displayhangman(wrong_guess,correct_guess,anime_character,hangman_body):
    if len(wrong_guess)<8:
        print(hangman_body[len(wrong_guess)])

        print('Wrong guesses:',end='')
        for wrong in wrong_guess:
            print(wrong,end='')
        print('')

        blanks = "_" * len(anime_character)

        for i in range(len(anime_character)):
            if anime_character[i] in correct_guess:
                blanks = blanks[:i] + anime_character[i] + blanks[i+1:]

        for letters in blanks:
            print(letters,end='')
        print('')

def guessTaken(alreadyexist):
    while True:
        guess = input('\n Start guessing:').lower()
        if guess not in string.ascii_lowercase:
            guess = input('Enter valid guess:')
        if not len(guess)== 1:
            guess=input('Enter a single character:')
        if guess==alreadyexist:
            guess=input('Guess again,guess already exist:')
        else:
            return guess

def playagain():
    again = input('Do you want to play again(Y/n)?').lower()
    if again.startswith('y'):
        return True
    else:
        return False

print('Anime Hangman')
characters="jabamiyumeko,ishigamisenku,satomemary,darkness,nifuji,narumi,koyanagi,kabakura,megumin,sabo,sukuna,gojo,yuji" \
           "sakatagintoki,shinpachi,kagura,hijikata,makisekurisu,light,l,karma,kageyama," \
           "kazuma,okabe,hachiman,yukino,yui,orekihotaru,chitandaeru,narutouzumaki," \
           "monkeydLuffy,Lelouch,tatsumi,esdeath,akame,arima,kaori,fujinuma,kakeru,naho," \
           "suwa,ichigokurosaki,uryuishida,giyuutomika,kenkaneki,saiki,zerotwo,hiro,chizuru,shuohuma,jintan,menma,norman," \
           "ray,emma,sakakibara,akira,maisakurajima,sakuta,Ayanokouji,suzune,roronoazoro," \
           "vinsmokesanji,boahancock,hinatahyuga,sasukeuchiha,CC,tenma,johan,,suzakukururugi," \
           "karen,shikamarunara,kakashihatake,itachi uchiha,tanjiro,zenitsu,deku" \
           "inosuke,portazdace,jiraiya,minato,god yato,hiyori,yukine,leviackerman,erenyeager," \
           "mikasaackerman,erwinsmith,edwardelric,alphonseelric,roymustang,kenma,oikawa,bokuto,erza" \
           "rayleigh,shanks,trafalgarlaw,killua,gon,hisoka,komi,ginko,natsu,goku,vegeta".lower().split(',')

wrong_guess = ''
correct_guess = ''
anime_character = random.choice(characters)
finish=False
streaks=0

while True:
    displayhangman(wrong_guess, correct_guess,anime_character,hangman_body)
    guess=guessTaken(wrong_guess+correct_guess)
    if guess in anime_character:
        correct_guess = correct_guess + guess
        complete = True
        for i in range(len(anime_character)):
            if anime_character[i] not in correct_guess:
                complete = False
                break
        if complete:
            streaks=streaks+1
            print(f'The Anime character is {anime_character}, You guessed it right')
            print('Winning Streaks:',streaks)
            finish = True
    else:
        wrong_guess = wrong_guess + guess
        if len(wrong_guess) == len(hangman_body) - 1:
            displayhangman(hangman_body, wrong_guess, correct_guess,anime_character)
            print(f'Oops!!...You are out of guesses, the anime character was {anime_character}')
            streaks=0
            finish = True

    if finish:
        if playagain():
            wrong_guess = ''
            correct_guess = ''
            finish = False
            anime_character = random.choice(characters)
        else:
            print("Thank you playing")
            break
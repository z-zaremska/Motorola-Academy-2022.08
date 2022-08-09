import os
os.system('cls')


#Import pliku z listą słów + utworzenie z nich listy
with open('Words.txt') as words_file:
    words_for_game = words_file.read()

list_of_words = words_for_game.split('\n')


#Personalizacja - przywitanie gracza
user_name = input('What is yout name?\n')

print(f"""\nHi, {user_name}!
Before we start, please choose difficulty level.
* Easy (type 'E')
* Hard (type 'H')""")


#Rozpoczęcie gry - wybór poziomu trudności.
game_start = True
while game_start:
    difficulty_level = input('\nChoose difficulty level:\nYour answear: ')
    if difficulty_level.lower() == 'q':
        print('\nYou have exit the game.')
        break
    elif difficulty_level.lower() == 'e':
        print('\nYou have chosen "easy" level.')
        break
    elif difficulty_level.lower() == 'h':
        print('\nYou have chosen "hard" level.')
        break
    else:
        print("""\nPlease choose difficulty level - easy('E')/hard('H').\nIf you want to quit the game, type 'Q'.""")



#Gra - poziom EASY

#Schemat
#—-----------------------------------
#Level: easy
#Guess chances: 10
#1 2 3 4
#A X X X X
#B X X X X
#—-----------------------------------







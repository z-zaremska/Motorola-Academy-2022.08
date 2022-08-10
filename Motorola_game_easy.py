import os
os.system('cls')

import random

#Import pliku z listą słów + utworzenie z nich listy
with open('Words.txt') as words_file:
    words_for_game = words_file.read()

list_of_words = words_for_game.split('\n')


#Zdefiniowanie funkcji wykorzystywanych w grze
def draw_words_for_game(list_of_words):
    """Randomly chooses 4 different words to reveal during the game."""
    for i in range(0,4):
        random_word = list_of_words.pop(random.randint(0, len(list_of_words)))
        words_in_game.append(random_word)
        words_in_game.append(random_word)


def update_board(guess_chances, round_0):
    """Clears previous game board and shows new one
    with updated game status."""
    import os
    os.system('cls')

    updated_board = f"""\nLevel: easy
Guess chances: {guess_chances}
Round: {10-guess_chances}
—-----------------------------------
_ 1 2 3 4
A {round_0['a1'][0]} {round_0['a2'][0]} {round_0['a3'][0]} {round_0['a4'][0]}
B {round_0['b1'][0]} {round_0['b2'][0]} {round_0['b3'][0]} {round_0['b4'][0]}
—-----------------------------------
"""
    print(updated_board)

def set_random_word():
    """Choses random word and removes it from words in game list."""
    random_word = random.choice(words_in_game)
    words_in_game.remove(random_word)
    return random_word


def uncover(user_choice):
    """Changes 'X' into 'word' from words_in_game."""
    return round_0[user_choice][1]


def cover(user_choice):
    """Changes 'word' from words_in_game into 'X'."""
    return round_0[user_choice][2]


def pick_first_word(user_choice_A):
    """Uncovers first word chosen by player."""
    round_0[user_choice_A][0] = uncover(user_choice_A)


def pick_maching_word(guess_chances, user_choice_A, user_choice_B):
    if round_0[user_choice_B][1] == round_0[user_choice_A][1]:
        round_0[user_choice_B][0] = uncover(user_choice_B)
        update_board(guess_chances, round_0)
        print(f'\nCongratulations!\nYou have uncoverd a pair of "{round_0[user_choice_B][1]}"')
        uncovered_pairs.append({round_0[user_choice_B][1]})
        go_on = input('\nIf you want to continue: press any.\nIf you want to quit press "q".\nYour answear: ')
        if go_on.lower() == 'n':
            print('\nGame over.')
    else:
        round_0[user_choice_B][0] = uncover(user_choice_B)
        update_board(guess_chances, round_0)
        print(f"""\nYou've uncovered word '{round_0[user_choice_B][1]}' ({user_choice_B}).
Unfortunately it's not the same as the one you've uncoverd last time: '{round_0[user_choice_A][1]}' ({user_choice_A}).""")
        go_on = input('\nIf you want to continue: press any.\nIf you want to quit press "q".\nYour answear: ')
        if go_on.lower() == 'n':
            print('\nGame over.')
        round_0[user_choice_A][0] = cover(user_choice_A)
        round_0[user_choice_B][0] = cover(user_choice_B)

    

#Game setup (Round 0)
#Choose random 4 words for the game.
uncovered_pairs = []
words_in_game = []
draw_words_for_game(list_of_words)
#Start chances
guess_chances = 10
#Prepare game board
round_0 = {
    'a1': ['X', set_random_word(), 'X'],
    'a2': ['X', set_random_word(), 'X'],
    'a3': ['X', set_random_word(), 'X'],
    'a4': ['X', set_random_word(), 'X'],
    'b1': ['X', set_random_word(), 'X'],
    'b2': ['X', set_random_word(), 'X'],
    'b3': ['X', set_random_word(), 'X'],
    'b4': ['X', set_random_word(), 'X'],
}

#Gameplay (Rounds 1-10 -> 5x Round A + Round B)
while True:
    #Round A
    update_board(guess_chances, round_0)   
    user_choice_A = input("""Which "X" you want to uncover?
Your answear: """)
    guess_chances -= 1
    pick_first_word(user_choice_A)
    #Round B
    update_board(guess_chances, round_0)
    user_choice_B = input("""Which "X" you want to uncover?
Your answear: """)
    guess_chances -= 1
    pick_maching_word(guess_chances, user_choice_A, user_choice_B)

    if len(uncovered_pairs) == 4:
        print('\nYOU WON!')
        break

    elif guess_chances == 0:
        print('\nGAME OVER')
        print(f'You have uncovered: {uncovered_pairs}')
        break

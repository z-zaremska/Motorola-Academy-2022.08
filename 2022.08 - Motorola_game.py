import os
import random
import time

#Import the words.txt file and convert it into list of words
with open('Words.txt') as words_file:
    words_for_game = words_file.read()

list_of_words = words_for_game.split('\n')

#Functions for gameplay
def draw_words_for_game(list_of_words, level):
    """Randomly chooses proper amount of different words (depending on
    chosen level) to reveal during the game."""
    if level == 'easy':
        amount_of_words = 4
    elif level == 'hard':
        amount_of_words = 8

    for i in range(0, amount_of_words):
        random_word = list_of_words.pop(random.randint(0, len(list_of_words)-1))
        words_in_game.append(random_word)
        words_in_game.append(random_word)


def update_board(round_0):
    """Clears previous game board and shows new one
    with updated game status at level easy."""
    os.system('cls')

    if level == 'easy':
        updated_board = f"""\nLevel: {level}
        Guess chances: {guess_chances}
        —-----------------------------------
        _ 1 2 3 4
        A {round_0['a1'][0]} {round_0['a2'][0]} {round_0['a3'][0]} {round_0['a4'][0]}
        B {round_0['b1'][0]} {round_0['b2'][0]} {round_0['b3'][0]} {round_0['b4'][0]}
        —-----------------------------------
        """
    elif level == 'hard':
        updated_board = f"""\nLevel: {level}
        Guess chances: {guess_chances}
        —-----------------------------------
        _ 1 2 3 4
        A {round_0['a1'][0]} {round_0['a2'][0]} {round_0['a3'][0]} {round_0['a4'][0]}
        B {round_0['b1'][0]} {round_0['b2'][0]} {round_0['b3'][0]} {round_0['b4'][0]}
        C {round_0['c1'][0]} {round_0['c2'][0]} {round_0['c3'][0]} {round_0['c4'][0]}
        D {round_0['d1'][0]} {round_0['d2'][0]} {round_0['d3'][0]} {round_0['d4'][0]}
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
    possible_choices.remove(user_choice_A)


def pick_maching_word(user_choice_A, user_choice_B):
    """"""
    if round_0[user_choice_B][1] == round_0[user_choice_A][1]:
        round_0[user_choice_B][0] = uncover(user_choice_B)
        possible_choices.remove(user_choice_B)
        update_board(round_0)
        print(f'\nCongratulations!\nYou have uncoverd a pair of "{round_0[user_choice_B][1]}"')
        uncovered_pairs.append({round_0[user_choice_B][1]})
        go_on = input('\nIf you want to continue: press any.\nIf you want to quit press "q".\nYour answear: ')
        if go_on.lower() == 'q':
            print('\nGame over.')
    else:
        round_0[user_choice_B][0] = uncover(user_choice_B)
        update_board(round_0)
        possible_choices.append(user_choice_A)
        print(f"""\nYou've uncovered word '{round_0[user_choice_B][1]}' ({user_choice_B}).
Unfortunately it's not the same as the one you've uncoverd last time: '{round_0[user_choice_A][1]}' ({user_choice_A}).""")
        go_on = input('\nIf you want to continue: press any.\nIf you want to quit press "q".\nYour answear: ')
        if go_on.lower() == 'q':
            print('\nGame over.')
        round_0[user_choice_A][0] = cover(user_choice_A)
        round_0[user_choice_B][0] = cover(user_choice_B)

level = ''
guess_chances = ''
uncovered_pairs = []
words_in_game = []
possible_choices = []

#Player introduction
user_name = input('What is yout name?\n')

print(f"""\nHi, {user_name.title()}!
Welcome to the simple 'Memory' game!
Your goal is to uncover all words pairs during the game!

Before we start, please choose difficulty level.
* Easy (type 'E')
* Hard (type 'H')""")

#Game setup
active = True
while active:
    difficulty_level = input('\nChoose difficulty level:\nYour answear: ')
    if difficulty_level.lower() == 'e':
        print('\nYou have chosen "easy" level.')
        level = 'easy'
        guess_chances = 10
        draw_words_for_game(list_of_words, level)
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
        possible_choices = ['a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4']
        break
    if difficulty_level.lower() == 'h':
        print('\nYou have chosen "hard" level.')
        level ='hard'
        guess_chances = 15
        draw_words_for_game(list_of_words, level)
        round_0 = {
            'a1': ['X', set_random_word(), 'X'],
            'a2': ['X', set_random_word(), 'X'],
            'a3': ['X', set_random_word(), 'X'],
            'a4': ['X', set_random_word(), 'X'],
            'b1': ['X', set_random_word(), 'X'],
            'b2': ['X', set_random_word(), 'X'],
            'b3': ['X', set_random_word(), 'X'],
            'b4': ['X', set_random_word(), 'X'],
            'c1': ['X', set_random_word(), 'X'],
            'c2': ['X', set_random_word(), 'X'],
            'c3': ['X', set_random_word(), 'X'],
            'c4': ['X', set_random_word(), 'X'],
            'd1': ['X', set_random_word(), 'X'],
            'd2': ['X', set_random_word(), 'X'],
            'd3': ['X', set_random_word(), 'X'],
            'd4': ['X', set_random_word(), 'X'],
            }
        possible_choices = ['a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4', 'c1', 'c2', 'c3', 'c4', 'd1', 'd2', 'd3', 'd4']
        break
    else:
        print("""\nPlease choose difficulty level - easy('E')/hard('H').""")

#Gameplay
while True: 
    #Round A
    update_board(round_0)
    while True:
        user_choice_A = input("""Which "X" you want to uncover?
Your answear: """)
        if user_choice_A.lower() in possible_choices:
            pick_first_word(user_choice_A)
            break
        else:
            print(f"\nYou can't choose {user_choice_A} - try again!")
    #Round B
    update_board(round_0)
    while True:
        user_choice_B = input("""Which "X" you want to uncover?
Your answear: """)
        if user_choice_B.lower() in possible_choices:
            guess_chances -= 1
            pick_maching_word(user_choice_A, user_choice_B)
            break
        else:
            print(f"\nYou can't choose {user_choice_B} - try again!")
    
    guessing_time = time.process_time()
    if level == 'easy' and len(uncovered_pairs) == 4:
        print(f"""\nYOU WON!
    It took you {10-guess_chances} chances and {guessing_time} seconds to win this game.""")
        break
    if level == 'hard' and len(uncovered_pairs) == 8:
        print(f"""\nYOU WON!
    It took you {15-guess_chances} chances and {guessing_time} seconds to win this game.""")
        break
    elif guess_chances == 0:
        print('\nGAME OVER')
        print(f'You have uncovered: {uncovered_pairs}')
        break

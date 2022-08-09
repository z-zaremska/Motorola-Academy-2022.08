import os
os.system('cls')

import random

#Import pliku z listą słów + utworzenie z nich listy
with open('Words.txt') as words_file:
    words_for_game = words_file.read()

list_of_words = words_for_game.split('\n')
words_in_game = []


#Zdefiniowanie funkcji wykorzystywanych w grze
def draw_words_for_game(list_of_words):
    """Randomly chooses 4 different words to reveal during the game."""
    for i in range(0,4):
        random_word = list_of_words.pop(random.randint(0, len(list_of_words)))
        words_in_game.append(random_word)
        words_in_game.append(random_word)


def use_chance(guess_chances):
    """Countdown guess chances"""
    guess_chances -= 1
    return guess_chances

def next_round(guess_chances, round_0, revealed_items):
    """Clears previous game board and shows new one
    with updated game status."""

    import os
    os.system('cls')

    next_round_board = f"""\nLevel: easy
    Guess chances: {guess_chances}
    You already revealed: {revealed_items}
    —-----------------------------------
    _ 1 2 3 4
    A {round_0['a1']} {round_0['a2']} {round_0['a3']} {round_0['a4']}
    B {round_0['b1']} {round_0['b2']} {round_0['b3']} {round_0['b4']}
    —-----------------------------------
    """
    print(next_round_board)

    

#Gra - poziom EASY

#Runda 0 - Początek gry
draw_words_for_game(list_of_words)
print(words_in_game)

guess_chances = 10
round_0 = {
    'a1': 'X',
    'a2': 'X',
    'a3': 'X',
    'a4': 'X',
    'b1': 'X',
    'b2': 'X',
    'b3': 'X',
    'b4': 'X',
}

print(f"""\nLevel: easy
    Guess chances: {guess_chances}
    —-----------------------------------
    _ 1 2 3 4
    A {round_0['a1']} {round_0['a2']} {round_0['a3']} {round_0['a4']}
    B {round_0['b1']} {round_0['b2']} {round_0['b3']} {round_0['b4']}
    —-----------------------------------
    """)

revealed_items = []

#Runda 1/10
first_user_choice = input("""Which "X" you want to reveal first?
Your answear: """)
round_0[first_user_choice] = random.choice(words_in_game)
revealed_items.append(first_user_choice)
guess_chances = use_chance(guess_chances)


#Rundy 2 - 9
have_chances = True
while have_chances:
    next_round(guess_chances, round_0, revealed_items)
    next_user_choice = input("""Which "X" you want to reveal next?
    Your answear: """)
    round_0[next_user_choice] = random.choice(words_in_game)
    revealed_items.append(next_user_choice)
    guess_chances = use_chance(guess_chances)
    if guess_chances == 0:
        next_round(guess_chances, round_0, revealed_items)
        have_chances = False

print('[GAME OVER] You have lost.')


# Hangman Challenge
# Author: Osiro Asunde

import random

listOfWords = ["dave", "fork", "spin", "isle", "bake", "tube", "cake", "cube", "tape", "cape", "late"]

word = random.choice(listOfWords)

display_word = ['_'] * len(word)
lives = 6
while True:
    letter = input("Guess a letter in the word: ").lower()

    correct_guess = False

    for i in range(len(word)):
        if letter == word[i]:
            correct_guess = True
            display_word[i] = letter

    print(' '.join(display_word))

    if not correct_guess:
        lives -= 1
        print(f"Nope, not in there. {lives} lives left.")

    if lives == 0:
        print("You lost!")
        break
    elif '_' not in display_word:
        print("Congratulations! You guessed the word.")
        break

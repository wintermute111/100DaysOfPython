import random
from hangman_words import word_list
from hangman_art import *
from replit import clear

lives = 6
word = random.choice(word_list)
display = []
guesses = []
for letter in word:
    display.append("_")
print(logo)
print("Here is your word: ")
print(display)

while ("_" in display) and (lives > 0):
    guess = input("Guess a letter: ").lower()
    if guess in guesses:
        print(f"You have already guessed {guess}, please try again.")
        continue
    clear()
    guesses.append(guess)
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print(f"Sorry, {guess} is not in the word.")
        lives -= 1

    print(display)
    print(stages[lives])
    if "_" not in display:
        print("YOU WIN")
    if lives == 0:
        print("YOU LOSE")

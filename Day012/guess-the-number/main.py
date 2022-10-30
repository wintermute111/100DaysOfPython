# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random
from replit import clear


def generate_answer():
    return random.randint(1, 100)


def get_guess():
    return int(input("Guess an integer from 1 to 100: "))


def game_mode():
    mode = input("Would you like 'easy' 10 guesses mode or 'hard' 5 guesses mode? (easy/hard) ").lower()
    if mode == "hard":
        return 5
    else:
        return 10


play_again = True
while play_again:
    print(logo)
    answer = generate_answer()
    guesses_remaining = game_mode()
    guessed = False
    while not guessed and guesses_remaining > 0:
        print(f"Guesses remaining: {guesses_remaining}")
        guess = get_guess()
        if guess == answer:
            guessed = True
            print(f"You guessed it! The answer was {answer}.")
        elif guess > answer:
            print("Too high.")
            guesses_remaining -= 1
        elif guess < answer:
            print("Too low.")
            guesses_remaining -= 1

    if guesses_remaining == 0:
        print("You ran out of guesses.")
    if input("Would you like to play again? (y/n) ").lower() == "y":
        clear()
    else:
        play_again = False
        print("Thanks for playing.")

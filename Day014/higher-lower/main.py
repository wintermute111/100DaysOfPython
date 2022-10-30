import random
from art import logo, vs
from game_data import data
from replit import clear

play_again = True
while play_again:
    score = 0
    choiceA = random.choice(data)
    choiceB = choiceA
    keep_going = True
    while keep_going:
        clear()
        print(logo)
        if score > 0:
            print(f"Your're right! Current score is {score}")
        print(f"Compare A: {choiceA['name']}, {choiceA['description']}, from {choiceA['country']}")
        print(vs)
        while choiceA == choiceB:
            choiceB = random.choice(data)
        print(f"Against B: {choiceB['name']}, {choiceB['description']}, from {choiceB['country']}")
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if choice == 'a':
            if choiceA["follower_count"] > choiceB["follower_count"]:
                score += 1
            else:
                keep_going = False
        else:
            if choiceB["follower_count"] > choiceA["follower_count"]:
                score += 1
            else:
                keep_going = False
        choiceA = choiceB
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    if input("Play again? (y/n) ") == "n":
        play_again = False

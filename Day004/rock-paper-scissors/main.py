import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

choices = ["rock", "paper", "scissors"]
computer = choices[random.randint(0, 2)]
you = input("rock, paper, or scissors? ").lower()

print("You: ")
if you == "rock":
    print(rock)
elif you == "paper":
    print(paper)
elif you == "scissors":
    print(scissors)
else:
    print("Not a valid choice.")

print("Computer:")
if computer == "rock":
    print(rock)
elif computer == "paper":
    print(paper)
else:
    print(scissors)

if you == computer:
    print("You Tie")
elif you == "rock" and computer == "paper":
    print("You Lose")
elif you == "rock" and computer == "scissors":
    print("You Win")
elif you == "paper" and computer == "rock":
    print("You Win")
elif you == "paper" and computer == "scissors":
    print("You Lose")
elif you == "scissors" and computer == "rock":
    print("You Lose")
elif you == "scissors" and computer == "paper":
    print("You Win")
else:
    print("You may have made a typo")

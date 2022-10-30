# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))

characters = ""
password = ""

if num_letters > 0:
    for i in range(1, num_letters + 1):
        characters += letters[random.randint(0, len(letters) - 1)]

if num_symbols > 0:
    for i in range(1, num_symbols + 1):
        characters += symbols[random.randint(0, len(symbols) - 1)]

if num_numbers > 0:
    for i in range(1, num_numbers + 1):
        characters += numbers[random.randint(0, len(numbers) - 1)]

for i in range(1, len(characters) + 1):
    rand_char = characters[random.randint(0, len(characters) - 1)]
    password += rand_char
    characters = characters.replace(rand_char, '', 1)

print(f"Your new password is: {password}")

# can improve by using random.choice to select your letters/symbols/numbers from the given lists and then use
# random.sample(string,len(string)) to shuffle the string.

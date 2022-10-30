def caesar(text, shift, direction):
    if direction == "decode":
        shift *= -1
    end_text = ''
    for letter in text:
        end_text += alphabet[(alphabet.index(letter) + shift) % 26]
    print(f"The {direction}d text is {end_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
again = True

while again:
    cipher_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    message = input("Type your message:\n").lower()
    shift_number = int(input("Type the shift number:\n"))
    caesar(message, shift_number, cipher_direction)
    cont = input("Would you like to run again? (yes or no) ").lower()
    if cont == "no":
        again = False

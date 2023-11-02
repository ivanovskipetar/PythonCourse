alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

from operator import *


def caesar(text, shift, direction):
    plain_text = ""
    if direction == 'encode':
        sign = "+"
    else:
        sign = "-"
    operation = {'+': add, '-': sub}

    for character in text:
        if character in alphabet:
            position_of_character = alphabet.index(character)
            encrypted_character = alphabet[(operation[sign](position_of_character, shift)) % 26]
            plain_text += encrypted_character
        else:
            plain_text += character

    print(f"The {direction}d text is {plain_text}")


while True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    if input("Type \'yes\' if you want to go again.Otherwise,type \'no\'" + "\n").lower() == "no":
        print("Goodbye")
        break

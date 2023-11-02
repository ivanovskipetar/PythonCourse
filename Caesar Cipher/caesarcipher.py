alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
        position_of_letter = alphabet.index(letter)
        encrypted_letter = alphabet[(position_of_letter + shift) % 26]
        encrypted_text += encrypted_letter
    print(f"The encoded text is {encrypted_text}")


# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text, shift):
    # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount
    # and print the decrypted text.
    # e.g.
    # cipher_text = "mjqqt"
    # shift = 5
    # plain_text = "hello"
    # print output: "The decoded text is hello"
    decrypted_text = ""
    for letter in text:
        position_of_letter = alphabet.index(letter)
        encrypted_letter = alphabet[(position_of_letter - shift) % 26]
        decrypted_text += encrypted_letter
    print(f"The decoded text is {decrypted_text}")


# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
# Then call the correct function based on that 'drection' variable.
# You should be able to test the code to encrypt *AND* decrypt a message.
i = 2
while (i > 0):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        encrypt(text, shift)
    else:
        decrypt(text, shift)
    i -= 1

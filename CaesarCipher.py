from art import logo

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def caesar(text, shift, direction):
    cipher_text = ''
    shift = shift % 26
    if direction == 'decode':
        shift *= -1  # Corrected placement
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_pos = (position + shift) % 26
            cipher_text += alphabet[new_pos]
        else:
            cipher_text += letter
    print(f"The {direction}d text is {cipher_text}.")

def restart_program():
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        caesar(text=text, shift=shift, direction=direction)
        
        reset = input('Type "yes" if you want to go again. Otherwise type "no".\n')
        if reset == 'no':
            print("Goodbye.")
            break

print(logo)
restart_program()

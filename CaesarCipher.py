alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text_input, shift_input, direction_input):
    new_text = ""
    for letter in text_input:
        position = alphabet.index(letter)
        if direction_input == 'encode':
            if position + shift_input > 25:
                new_position = position + shift_input - 26
            else:
                new_position = position + shift_input
            new_text += alphabet[new_position]
        elif direction_input == 'decode':
            if position - shift_input < 0:
                new_position = 26 + shift_input - position
            else:
                new_position = position - shift_input
            new_text += alphabet[new_position]
    print(f"The {direction_input}d text is {new_text}")

            
caesar(text, shift, direction)

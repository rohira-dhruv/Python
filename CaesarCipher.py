alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text, shift, direction):
    new_text = ""
    for letter in text:
        position = alphabet.index(letter)
        if direction == 'encode':
            if position + shift > 25:
                new_position = position + shift - 26
            else:
                new_position = position + shift
            new_text += alphabet[new_position]
        elif direction == 'decode':
            if position - shift < 0:
                new_position = 26 + shift - position
            else:
                new_position = position - shift
            new_text += alphabet[new_position]
    print(f"The {direction}d text is {new_text}")

            
caesar(text, shift, direction)


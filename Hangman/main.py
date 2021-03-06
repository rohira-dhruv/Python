
import random
import os
from data import word_list_hangman
from art import logo_hangman
from art import stages_hangman


def clear():
    os.system('cls')


chosen_word = random.choice(word_list_hangman)
word_length = len(chosen_word)
end_of_game = False
lives = 6
print(logo_hangman)

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
        print(f"You've already guessed {guess}")
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was {chosen_word}")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages_hangman[lives])

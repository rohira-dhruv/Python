from art import logo_number_guesser
import os
import random


def clear():
    """This function is used to clear the terminal for a better user experience."""
    os.system('cls')


def guess(guessed_number, chosen_number):
    """This function gives a response whether the guess is more than, less than or incorrect."""
    if guessed_number > chosen_number:
        print("Too High.")
        return 'H'
    elif guessed_number < chosen_number:
        print("Too Low.")
        return 'L'
    else:
        return 'C'


def play_game():
    print(logo_number_guesser)
    print("Welcome to The Number Guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    difficulty = input("Choose the difficulty, 'easy' or 'hard': ").lower()
    if difficulty == 'hard':
        no_of_guesses = 5
    else:
        no_of_guesses = 10

    end_game = False
    random_number = random.randint(1, 100)
    while not end_game and no_of_guesses > 0:
        print(f"You have {no_of_guesses} guesses remaining to guess the number.")
        guessed_number = int(input("Make a guess: "))
        response = guess(guessed_number, random_number)
        if response == 'H' or response == 'L':
            no_of_guesses -= 1
            if no_of_guesses == 0:
                print("You failed to guess the number. Better luck next Time")
                print(f"The number was {random_number}")
            else:
                print("Guess Again.")
        elif response == 'C':
            end_game = True
            print(f"You got it! The answer was {random_number}")


restart_game = 'y'
while restart_game == 'y':
    clear()
    play_game()
    restart_game = input("Do you want to play the Game again? Type 'y' for yes and 'n' for no: ")
print("Thank you for Playing! Have a Nice Day")

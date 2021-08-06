import random
import os
from art import rock, paper, scissors


def clear():
    os.system('cls')

def play_game():
    print("Welcome to the game of Rock Paper Scissors")
    end_game = False
    while not end_game:    
        user_choice = int(input("Enter 0 for Rock, 1 for Paper and 2 for Scissors\n"))
        options = [rock, paper, scissors]
        if 0 <= user_choice <= 2:
            print("You chose:\n"+options[user_choice])
            comp_choice = random.randint(0, 2)
            print("the Computer Chose: \n")
            print(options[comp_choice])
            if comp_choice-user_choice == 1 or comp_choice-user_choice == -2:
                print("You lose")
            elif comp_choice == user_choice:
                print("It is a tie")
            else:
                print("You win")
        else:
            print("Please enter the correct option")
        if input("Do you want to play the game again? Type 'y' for yes or 'n' for no: ").lower() == 'n':
            end_game = True
        clear()
    print("Thank you for playing!")


play_game()

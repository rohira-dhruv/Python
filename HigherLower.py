import random
from art import logo_higher_lower, vs
from data import data_higher_lower
import os


def clear():
    """This function is used to clear the terminal for a better user experience."""
    os.system('cls')


def get_item(data_list, removal_list):
    """This function retrieves a randomly picked item form data_list and adds it to removal_list."""
    item = data_list[random.randint(0, len(data_list))]
    removal_list.append(item)
    data_list.remove(item)
    return item


def compare(item_A, item_B):
    """This function checks which item has more followers and returns 'A' or 'B' accordingly."""
    if item_A['follower_count'] >= item_B['follower_count']:
        return 'A'
    else:
        return 'B'


def game():
    removed_items = []
    end_game = False
    score = 0
    item_A = get_item(data_higher_lower, removed_items)
    while not end_game:
        print(logo_higher_lower)
        item_B = get_item(data_higher_lower, removed_items)
        print(f"Compare A: {item_A['name']}, a {item_A['description']}, from {item_A['country']}")
        print(vs)
        print(f"Against B: {item_B['name']}, a {item_B['description']}, from {item_B['country']}")
        higher = input("Who has more followers? 'A' or 'B': ").upper()
        clear()
        if higher == compare(item_A, item_B):
            score += 1
            print(f"\nYou're right! The current score is: {score}")
        else: 
            end_game = True
            print(f"\nSorry that's wrong. Your final score is: {score}")
        item_A = item_B
    data_higher_lower.extend(removed_items)


game()







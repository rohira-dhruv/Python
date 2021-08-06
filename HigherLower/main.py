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


def compare(item_a, item_b):
    """This function checks which item has more followers and returns 'A' or 'B' accordingly."""
    if item_a['follower_count'] >= item_b['follower_count']:
        return 'A'
    else:
        return 'B'


def game():
    removed_items = []
    end_game = False
    score = 0
    item_a = get_item(data_higher_lower, removed_items)
    while not end_game:
        print(logo_higher_lower)
        item_b = get_item(data_higher_lower, removed_items)
        print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}")
        print(vs)
        print(f"Against B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}")
        higher = input("Who has more followers? 'A' or 'B': ").upper()
        clear()
        if higher == compare(item_a, item_b):
            score += 1
            print(f"\nYou're right! The current score is: {score}")
        else: 
            end_game = True
            print(f"\nSorry that's wrong. Your final score is: {score}")
        item_a = item_b
    data_higher_lower.extend(removed_items)


game()

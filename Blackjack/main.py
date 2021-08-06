
from art import logo_blackjack
import os
import random


def clear():
    """This function is used to clear the terminal window for a better user experience"""
    os.system('cls')


def deal_card():
    """This function returns a randomly drawn card from a deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(card_list):
    """This function returns the score of the hand dealt"""
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
    elif sum(card_list) > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)


def compare(user_cards, dealer_cards):
    """This function compares the score between two set of cards and prints the result"""
    if calculate_score(user_cards) == 0 or calculate_score(user_cards) == 21:
        if calculate_score(dealer_cards) == 0 or calculate_score(dealer_cards) == 21:
            print("It is a Draw!")
        else:
            print("BLACKJACK! You Win 🎉")
    elif calculate_score(user_cards) < 21:
        if calculate_score(dealer_cards) > 21:
            print("The Computer went over. You Win 😁")
        elif calculate_score(dealer_cards) < calculate_score(user_cards):
            print("You Win 😃")
        elif calculate_score(dealer_cards) == calculate_score(user_cards):
            print("It is a Draw!")
        else:
            print("You Lose 😭")
    else:
        print("You went over. You Lose 😤")
    

def play_game():
    print(logo_blackjack)
    user_cards = []
    dealer_cards = []
    decision = 'y'
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())
    user_score = user_cards[0]
    while decision == 'y' and user_score <= 21:
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)
        print(f"\tYour cards: {user_cards}, current score is: {user_score}")
        print(f"\tDealer's first card is: {dealer_cards[0]}")
        if user_score <= 21:
            decision = input("Type 'y' to get another card, 'n' to pass: ")
    dealer_score = dealer_cards[0]
    while dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)
    print(f"\tYour final hand is {user_cards} and the final score is: {user_score}")
    print(f"\tComputer's final hand is {dealer_cards} and the final score is {dealer_score}")
    compare(user_cards, dealer_cards)


while input("Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no: ").lower() == 'y':
    clear()
    play_game()
print("Thank you for playing!")

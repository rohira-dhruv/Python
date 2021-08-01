import os
from data import menu_coffee_machine, resources
from art import logo_coffee_machine


def clear():
    """This function is used to clear the terminal for a better user experience."""
    os.system('cls')


def report():
    """This function generates a report of the resources"""
    for item in resources:
        if item == "water" or item == "milk":
            print(f"{item.title()}: {resources[item]}ml")
        elif item == "coffee":
            print(f"{item.title()}: {resources[item]}g")
        elif item == "money":
            print(f"{item.title()}: ${resources[item]}")


def are_resources_sufficient(drink_type):
    """This function checks if the available resources are enough to make the given drink. Returns -1 if possible
     otherwise it returns the ingredient name that is insufficient. """
    ingredients_available = resources
    ingredients_needed = menu_coffee_machine[drink_type]["ingredients"]
    for ingredient in ingredients_needed:
        if ingredients_needed[ingredient] > ingredients_available[ingredient]:
            return ingredient
    return -1


def process_coins(quarters, dimes, nickels, pennies):
    """calculates the total money entered into the machine"""
    total = quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01
    return total


def is_transaction_successful(money, cost):
    """This function returns truth value based on whether transaction is possible"""
    if money >= cost:
        return True
    else:
        return False


def update_resources(drink_type):
    """This function updates the resources after making the drink_type."""
    for item in menu_coffee_machine[drink_type]["ingredients"]:
        resources[item] -= menu_coffee_machine[drink_type]["ingredients"][item]
    if drink_type == "espresso":
        resources["money"] += 1.50
    elif drink_type == "latte":
        resources["money"] += 2.50
    else:
        resources["money"] += 3.00


def get_coffee():
    print(logo_coffee_machine)
    is_on = True
    money = 0.0
    resources["money"] = money
    while is_on:
        direction = input("What would you like? (espresso/latte/cappuccino): ")
        if direction == "off":
            is_on = False
        elif direction == "report":
            report()
        elif direction == 'espresso' or direction == 'latte' or direction == 'cappuccino':
            if are_resources_sufficient(direction) == -1:
                print("Please insert coins.")
                nr_quarters = int(input("How many quarters? "))
                nr_dimes = int(input("How many dimes? "))
                nr_nickels = int(input("How many nickels? "))
                nr_pennies = int(input("How many pennies? "))
                money_entered = process_coins(nr_quarters, nr_dimes, nr_nickels, nr_pennies)
                if is_transaction_successful(money_entered, menu_coffee_machine[direction]["cost"]):
                    update_resources(direction)
                    if money_entered > menu_coffee_machine[direction]["cost"]:
                        change = money_entered - menu_coffee_machine[direction]["cost"]
                        print(f"Here is ${round(change,2)} in change.")
                    print(f"Here is your {direction}☕. Enjoy!")
                else:
                    print(f"Sorry that's not enough money. Money refunded.")

            else:
                print(f"Sorry there is not enough {are_resources_sufficient(direction)}")
    print("Thank you for using the machine😄. Have a good day!")


get_coffee()

from classes import *


def do_tavern(user: Player):
    print("You enter the tavern.\n")
    print("You can pay to spend the night to rest.\n")
    print("1. Pay 50.\n")
    print("2. Go back\n")
    # Request user input.
    tavern_choice = input("Enter your choice: ")
    # If the user chose to visit the tavern, check if they have enough money to rest.
    if tavern_choice == "1" and user.money >= 50:
        # If they have enough money, subtract the cost from their money and set their hp to full.
        user.money -= 20
        user.hp = 100
        print("You pay $50 and rest for the night.\n")
        print(f"You have $" + {user.money} + " left.\n")
        # Return the user to the town.
        return Location.TOWN
    elif tavern_choice == "1" and user.money < 50:
        print("You don't have enough money to pay.\n")
        # Return the user to the town.
        return Location.TOWN
    elif tavern_choice == "2":
        print("You leave the tavern.\n")
        # Return the user to the town.
        return Location.TOWN

    # If the user chose to go back, return to the town.
    elif tavern_choice == 2:
        print("You leave the tavern.\n")
        return Location.TOWN

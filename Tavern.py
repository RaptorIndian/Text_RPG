from classes import *


def do_tavern(user: Player):
    print("You enter the tavern.\n")
    print("You can pay to spend the night to rest or buy some cooked food.\n")
    print("1. Pay $20 for a night.\n")
    print("2. Pay $12 for cooked food.\n")
    print("3. Go back\n")

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

    elif tavern_choice == "2":
        food_choice = int(input("How much food would you like to buy? "))
        if food_choice > 0 and user.carry_weight + food_choice > user.carry_weight:
            # Check the player's inventory to see if they have any of this food type.
            if "cooked food" in user.inventory:
                # If they have some already, add the amount to their inventory.
                user.inventory["Cooked Beef"].amount += food_choice
                # Subtract the cost from their money.
                user.money -= food_choice * 12
            else:
                user.inventory.append(Food("Cooked Beef", 1, food_choice, 30))
                user.money -= food_choice * 12

    # If the user chose to go back, return to the town.
    elif tavern_choice == "3":
        print("You leave the tavern.\n")
        return Location.TOWN

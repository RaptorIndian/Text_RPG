from classes import *
from colorama import Fore, Style


def do_arena(user: Player):
    print("You enter the arena.\n")
    print("You can battle against others or train yourself.\n")
    print("1. Battle\n")
    print("2. Go back\n")
    arena_choice = input("Enter your choice: ")
    print("---------------------\n")

    if arena_choice == "1":
        # If the user chose to battle, create a gladiator.
        gladiator = Gladiator("The gladiator", 100, 10, 0, 10)
        battle(user, gladiator)

        # Depending on the outcome of the battle, print the results.
        if gladiator.hp <= 0:
            print("You won the battle! You received $10.\n")
            user.money += 50
            # Return the user to the town.
            return Location.TOWN
        elif user.hp <= 0:
            # Prints the state of the battle in red.
            print(Fore.RED + "-------------")
            print("You lost the battle!")
            print("-------------")
            # Return the color to the default.
            print(Style.RESET_ALL)
            # Return the user to the town.
            return Location.TOWN

    elif arena_choice == "2":
        print("You leave the arena.\n")
        # Return the user to the town.
        return Location.TOWN

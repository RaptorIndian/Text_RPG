from classes import *
from weapons import *


def do_arena(user: Player):
    print("You enter the arena.\n")
    print("You can battle against others for money.\n")
    print("1. Battle\n")
    print("2. Go back\n")
    arena_choice = input("Enter your choice: ")
    print("---------------------\n")

    if arena_choice == "1":
        # If the user chose to battle, create a gladiator.
        skill = random.randint(1, 10)
        gladiator = Unit("The gladiator", 100, skill, 2, [], None, fists, None)
        user.location = battle(user, gladiator, user.location)

        # Depending on the outcome of the battle, print the results.
        if gladiator.hp <= 0:
            print("You won the battle! You received $10.\n")
            user.money += 50

            input("Press enter to continue. ")
            # Return the user to the town.
            return Location.TOWN
        elif user.hp < 4:
            # Prints the state of the battle in red.
            print("--------------------\n" + colorize_text("You lost the battle!\n",
                  "red") + "--------------------\n")
            input("Press enter to continue. ")
            # Return the user to the town.
            return Location.TOWN
        else:
            input("If you see this message, tell Rapta!")

    elif arena_choice == "2":
        print("You leave the arena.\n")
        # Return the user to the town.
        return Location.TOWN

    else:
        print("Invalid choice.\n")
        input("Press enter to continue.\n")
        return Location.ARENA

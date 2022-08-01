from classes import *


def do_town(user: Player):
    print("What would you like to do?\n---------------------\n")
    print("1. Go to the barracks\n")
    print("2. Go to the tavern\n")
    print("3. Go to the arena\n")
    print("4. Go to the shop\n")
    print("5. Check your stats\n")
    print("99. Quit?\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        return Location.BARRACKS

    elif choice == "2":
        return Location.TAVERN

    elif choice == "3":
        return Location.ARENA

    elif choice == "4":
        return Location.SHOP

    elif choice == "5":
        return Location.STATS

    elif choice == "99":
        return Location.QUIT

    else:
        print("Invalid choice.\n")
        input("Press enter to continue.\n")
        return Location.TOWN

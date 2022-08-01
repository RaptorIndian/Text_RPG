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
        user.location = Location.BARRACKS
        return Location.BARRACKS

    elif choice == "2":
        user.location = Location.TAVERN
        return Location.TAVERN

    elif choice == "3":
        user.location = Location.ARENA
        return Location.ARENA

    elif choice == "4":
        user.location = Location.SHOP
        return Location.SHOP

    elif choice == "5":
        user.location = Location.STATS
        return Location.STATS

    elif choice == "99":
        user.location = Location.QUIT
        return Location.QUIT

    else:
        print("Invalid choice.\n")
        input("Press enter to continue.\n")
        return Location.TOWN

from classes import *


def do_town(user: Player):
    print("What would you like to do?\n---------------------\n")
    print("1. Go to the barracks\n")
    print("2. Go to the tavern\n")
    print("3. Go to the arena\n")
    print("4. Check your stats\n")
    print("5. Quit?\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        return Location.BARRACKS

    elif choice == "2":
        print("Tavern is unimplemented.\n")
        return Location.TOWN

    elif choice == "3":
        return Location.ARENA

    elif choice == "4":
        print(user.name)
        print("---------------------\n")
        "name, hp, attack, defense, skill, money, army, location, weight, inventory"
        print(f"{user.name}")
        print(f"HP: {user.hp}")
        print(f"Attack: {user.attack}")
        print(f"Defense: {user.defense}")
        print(f"Skill: {user.skill}")
        print(f"Money: {user.money}")

        units = [soldier.__class__.__name__ for soldier in user.army]
        spear_amount = units.count("Spearman")
        knight_amount = units.count("Knight")
        final_amount = ""
        if spear_amount > 0:
            final_amount += f"\n{spear_amount} Spearman(s) "
        if knight_amount > 0:
            final_amount += f"\n{knight_amount} Knight(s) "
        print(
            f"Your army consists of {len(user.army)} units. {final_amount}\n")

        print(f"Location: {user.location}")
        print(f"Weight: {user.weight}")
        print(f"Inventory: {user.inventory}")

        input("Press enter to continue.\n")
        return Location.TOWN
    elif choice == "5":
        print("Quit is unimplemented?!")
        return Location.TOWN

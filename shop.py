from classes import *
from weapons import *
from armors import *
from foods import *


def do_shop(user: Player):
    print("You enter the shop.\n")
    print("You can buy items to help your character.\n")
    # Determine the amount of armor the shop has.
    chance = random.randint(2, 4)
    armor_selection = [gambeson for i in range(chance)]
    print("1. Armor\n")
    weapon_selection = [copper_sword, copper_axe]
    print("2. Weapons\n")
    food_selection = [apple]
    print("3. Food\n")
    print("4. Go back\n")

    choice = input("What would you like to browse?\n")

    if choice == "1":
        for armor in armor_selection:
            display_item_details(armor, user)
            return Location.SHOP

    elif choice == "2":
        for weapon in weapon_selection:
            display_item_details(weapon, user)
            return Location.SHOP

    elif choice == "3":
        for food in food_selection:
            display_item_details(food, user)
            return Location.SHOP

    elif choice == "4":
        return Location.TOWN

    else:
        print("Invalid choice.\n")
        return Location.SHOP
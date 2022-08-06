from classes import *
from weapons import *


def do_stats(user: Player, location_name: str):

    # Prints the user's name in the color cyan.
    print(colorize_text(user.name, "cyan"))

    # If the user's HP is less than 25, print the user's HP in red.
    if user.hp < 25:
        print(colorize_text(f"HP: {user.hp}", "red"))
    else:
        print(f"HP: {user.hp}")

    # Prints the user's weapon name.
    print(f"Weapon: {user.main_hand.name}")

    # Prints the user's attack against something with no armor.
    unit_2 = Unit("Dummy", 100, 1, 100, copper_axe, None, copper_sword, None)
    attack = damage_calc(user, unit_2)
    # If the damage is somehow 0 or less, set it to 1.
    print(f" Attack: {attack}")

    # Prints the user's main hand weapon skill.
    print(f" Weapon Skill: {user.main_hand.weapon_skill}")

    # Prints the user's defense.
    user.update_defense()
    print(f"Defense: {user.defense}")

    # Prints the user's skill.
    print(f"Skill: {user.combat_skill}")

    # Prints the user's money.
    print(f"Money: {user.money}")

    # Prints the user's carrying weight.
    print(f"Weight: {user.carry_weight}")

    # If the player has no items, it will print "Inventory: Empty".
    if len(user.inventory) == 0:
        print("Inventory: Empty")
    # Prints the user's inventory.
    else:
        for item in user.inventory:
            print(item.name)

    # Prints the name of the location the user is in.
    print(f"You are in: {location_name}.\n")

    # If the user has no units under their command, pass.
    if len(user.army) == 0:
        pass
    # If the user has less than 10 units under their command, print the number of units in their group.
    elif len(user.army) < 10:
        units = [soldier.__class__.__name__ for soldier in user.army]
        spear_amount = units.count("Spearman")
        knight_amount = units.count("Knight")
        final_amount = ""
        if spear_amount > 0:
            final_amount += f"\n{spear_amount} Spearman(s) "
        if knight_amount > 0:
            final_amount += f"\n{knight_amount} Knight(s) "
        print(f"Your group is {len(user.army)} units. {final_amount}")
    # If the user has more than 10 units under their command, print the number of units in their group.
    else:
        # Print the number of each type of unit in the user's army.
        units = [soldier.__class__.__name__ for soldier in user.army]
        spear_amount = units.count("Spearman")
        knight_amount = units.count("Knight")
        final_amount = ""
        if spear_amount > 0:
            final_amount += f"\n{spear_amount} Spearman(s) "
        if knight_amount > 0:
            final_amount += f"\n{knight_amount} Knight(s) "
        print(
            f"Your army consists of {len(user.army)} units.  {final_amount}")

    print("What would you like to do?\n")
    print("1. View weapons\n")
    print("2. View armor\n")
    print("3. View inventory\n")
    print("4. View army\n")
    print("5. Exit stats\n")

    choice = input("Enter your choice: ")
    print("---------------------\n")

    if choice == "1":
        # Prints the user's weapons.
        display_weapons(user)

    elif choice == "2":
        # Prints the user's armor.
        display_armor(user)

    elif choice == "3":
        # Prints the user's inventory.
        display_inventory(user)

    elif choice == "4":
        # Prints the user's army.
        display_army(user)

    elif choice == "5":
        # Exits the stats menu.
        return

    

    else:
        print("Invalid choice.\n")
        do_stats(user, location_name)


    return Location.TOWN

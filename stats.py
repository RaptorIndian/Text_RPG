from classes import *


def do_stats(user: Player, location_name: str):
    print("---------------------\n")
    # Prints the user's name in the color cyan.
    print(colorize_text(user.name, "cyan"))
    # If the user's HP is less than 25, print the user's HP in red.
    if user.hp < 25:
        colorize_text(f"HP: {user.hp}", "red")
    else:
        print(f"HP: {user.hp}")
    # Prints the user's attack.
    print(f"Attack: {user.attack}")
    # Prints the user's defense.
    print(f"Defense: {user.defense}")
    # Prints the user's skill.
    print(f"Skill: {user.skill}")
    # Prints the user's money.
    print(f"Money: {user.money}")
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
            f"Your army consists of {len(user.army)} units. {final_amount}")

    # Prints the user's carrying weight.
    print(f"Weight: {user.weight}")
    # If the player has no items, it will print "Inventory: Empty".
    if len(user.inventory) == 0:
        print("Inventory: Empty")
    else:
        for item in user.inventory:
            print(item.name)
    # Prints the name of the location the user is in.
    print(f"You are in: {location_name}.\n")

    input("Press enter to continue.\n")
    return Location.TOWN

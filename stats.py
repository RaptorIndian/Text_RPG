from turtle import update
from classes import *


def do_stats(user: Player, location_name: str):
    print("---------------------\n")

    # Prints the user's name in the color cyan.
    print(colorize_text(user.name, "cyan"))

    # If the user's HP is less than 25, print the user's HP in red.
    if user.hp < 25:
        print(colorize_text(f"HP: {user.hp}", "red"))
    else:
        print(f"HP: {user.hp}")

    # Prints the user's attack.
    # Increase the amount of damage a weapon does by the user's weapon skill with an exponential curve.
    attack = user.main_hand.base_damage + \
        pow(user.main_hand.weapon_skill, 1.13)
    attack = attack * 1.15
    attack = round(attack)
    # If the damage is somehow 0 or less, set it to 1.
    if attack <= 0:
        attack = 1
    print(f"Attack: {attack}")

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

    input("Press enter to continue.\n")
    return Location.TOWN

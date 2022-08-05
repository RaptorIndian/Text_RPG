from ast import Not
import random
from enum import Enum
from colorama import Fore, Style
import math


class Food:
    def __init__(self, name: str, weight: int, amount: int, hp_increase: int):
        self.name = name
        self.weight = weight
        self.amount = amount
        self.hp_increase = hp_increase


class Weapon:
    def __init__(self, name: str, weight: int, weapon_skill: int, base_damage: int, reach: int, bludgeon: int, slash: int, pierce: int, quality: int, exp: int = 0, poison: bool = False):
        self.name = name
        self.weight = weight
        self.weapon_skill = weapon_skill
        self.base_damage = base_damage
        self.reach = reach
        self.bludgeon = bludgeon
        self.slash = slash
        self.pierce = pierce
        self.quality = quality
        # Exp is an optional argument.
        self.exp = exp
        # Poison will be an optional argument.
        self.poison = poison


class Armor:
    def __init__(self, name: str, weight: int, defense: int, bludgeon_resist: int, slash_resist: int, pierce_resist: int):
        self.name = name
        self.weight = weight
        self.defense = defense
        self.bluegeon_resist = bludgeon_resist
        self.slash_resist = slash_resist
        self.pierce_resist = pierce_resist


class Location(Enum):
    TOWN = 1
    ARENA = 2
    BARRACKS = 3
    TAVERN = 4
    SHOP = 5
    STATS = 6
    QUIT = 99


class Player:
    def __init__(self, name: str, hp: int, defense: int, combat_skill: int, money: int, army: list, location: Location, carry_weight: int, weapons: list, equipped_armor: Armor, armors: list, inventory: list, main_hand: Weapon, off_hand: Weapon, reputation: int, playtime: int):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.combat_skill = combat_skill
        self.money = money
        self.army = army
        self.location = location
        self.carry_weight = carry_weight
        self.weapons = weapons
        self.equipped_armor = equipped_armor
        self.armors = armors
        self.inventory = inventory
        self.main_hand = main_hand
        self.off_hand = off_hand
        self.reputation = reputation
        self.playtime = playtime

    def low_hp(self):
        '''Prints the player's hp in the color red.'''
        print(Fore.RED + str(self.hp))
        print(Style.RESET_ALL)

    def update_defense(self):
        '''Updates the player's defense.'''
        if self.equipped_armor is not None:
            self.defense = self.equipped_armor.defense
        else:
            self.defense = 0


class Unit:
    def __init__(self, name: str, hp: int, defense: int, combat_skill: int, money: int, weapons: list, equipped_armor: Armor, main_hand: Weapon, off_hand: Weapon):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.combat_skill = combat_skill
        self.money = money
        self.weapons = weapons
        self.equipped_armor = equipped_armor
        self.main_hand = main_hand
        self.off_hand = off_hand


def colorize_text(text: str, color: str):
    '''Colorizes the text.'''
    color = color.lower()
    # If the color is red, return the text in red.
    if color == "red":
        return Fore.RED + text + Style.RESET_ALL

    # If the color is green, return the text in green.
    elif color == "green":
        return Fore.GREEN + text + Style.RESET_ALL

    # If the color is blue, return the text in blue.
    elif color == "blue":
        return Fore.BLUE + text + Style.RESET_ALL

    # If the color is yellow, return the text in yellow.
    elif color == "yellow":
        return Fore.YELLOW + text + Style.RESET_ALL

    # If the color is cyan, return the text in cyan.
    elif color == "cyan":
        return Fore.CYAN + text + Style.RESET_ALL


def display_item_details(item, user: Player):
    '''Displays an item's info.'''
    print("---------------------")
    print(f"{item.name}")
    if type(item) == Weapon:
        print(f"|Weight: {item.weight}")
        print(f"|Weapon Skill: {item.weapon_skill}")
        print(f"|Base Damage: {item.base_damage}")
        print(f"|Reach: {item.reach}")
        print(f"|Bludgeon: {item.bludgeon}")
        print(f"|Slash: {item.slash}")
        print(f"|Pierce: {item.pierce}")
        print(f"|Quality: {item.quality}")
        print(f"|Exp: {item.exp}")
        if item.poison:
            print(f"|Can use poison.")
        
        if user.main_hand == item:
            print("Currently equipped in main hand.")
        elif user.off_hand == item:
            print("\nCurrently equipped in off hand.")
        else:
            print("Not equipped.")

        # Ask the user if they want to equip the weapon.
        print("\nWould you like to manage this item?")
        print("1. Yes")
        print("2. No")
        choice = input("Choice: ")

        # If the user wants to equip the weapon.
        if choice == "1":
            # Check if the weapon is already equipped.
            if item == user.main_hand and item.name != "fists" or item == user.off_hand and item.name != "fists":
                # Ask if they want to unequip the weapon.
                print("\nDo you want to unequip this weapon?")
                print("1. Yes")
                if item == user.main_hand:
                    print("2. Move to off hand")
                elif item == user.off_hand:
                    print("2. Move to main hand")
                print("3. Cancel")
                choice = input("Choice: ")

                # If the user wants to unequip the weapon.
                if choice == "1":
                    if item == user.main_hand:
                        # Puts fists in main hand.
                        user.main_hand = user.weapons[0]
                    elif item == user.off_hand:
                        user.off_hand = user.weapons[0]
                    print("\nWeapon unequipped.")
                    input("Press enter to continue...")

                elif choice == "2":
                    # Move the weapon to the other hand.
                    if item == user.main_hand:
                        user.main_hand = user.off_hand
                        user.off_hand = item
                    elif item == user.off_hand:
                        user.off_hand = user.main_hand
                        user.main_hand = item
                    print("\nWeapon moved.")
                    input("Press enter to continue...")

                elif choice == "3":
                    return
            else:
                # Ask the user if they want to equip the weapon.
                print("\nDo you want to equip this weapon?")
                print("1. Equip to main hand")
                print("2. Equip to off hand")
                print("3. Cancel")
                choice = input("Choice: ")
                if choice == "1":
                    # Equip the weapon to the main hand.
                    user.main_hand = item
                    print("\nWeapon equipped to main hand.")
                    input("Press enter to continue...")
                elif choice == "2":
                    # Equip the weapon to the off hand.
                    user.off_hand = item
                    print("\nWeapon equipped to off hand.")
                    input("Press enter to continue...")
                elif choice == "3":
                    return

    if type(item) == Armor:
        print(f"|Weight: {item.weight}")
        print(f"|Defense: {item.defense}")
        print(f"|Bludgeon resistance: {item.bludgeon_resist}")
        print(f"|Slash resistance: {item.slash_resist}")
        print(f"|Pierce resistance: {item.pierce_resist}")

        if user.spare_armor is not None:
            if item in user.equipped_armor:
                print("Currently equipped.")
            else:
                print("Not equipped.")
        else:
            print("Not equipped.")
        print("\nWould you like to manage this item?")
        print("1. Yes")
        print("2. No")
        choice = input("Choice: ")
        if choice == "1":
            # Check if the armor is already equipped.
            if item in user.equipped_armor:
                # Ask if they want to unequip the armor.
                print("\nDo you want to unequip this armor?")
                print("1. Yes")
                print("2. Cancel")
                choice = input("Choice: ")
                if choice == "1":
                    # Unequip the armor.
                    user.equipped_armor = None
                    print("\nArmor unequipped.")
                    input("Press enter to continue...")
                elif choice == "2":
                    return
            else:
                # Ask the user if they want to equip the armor.
                print("\nDo you want to equip this armor?")
                print("1. Equip")
                print("2. Cancel")
                choice = input("Choice: ")
                if choice == "1":
                    # Equip the armor.
                    user.equipped_armor = item
                    print("\nArmor equipped.")
                    input("Press enter to continue...")
                elif choice == "2":
                    return



    elif type(item) == Armor:
        print(f"Weight: {item.weight}")
        print(f"Defense: {item.defense}")
        print(f"Bludgeon Resist: {item.bluegeon_resist}")
        print(f"Slash Resist: {item.slash_resist}")
        print(f"Pierce Resist: {item.pierce_resist}")

    elif type(item) == Food:
        print(f"Weight: {item.weight}")
        print(f"Amount: {item.amount}")
        print(f"HP Increase: {item.hp_increase}")


def display_weapons(user: Player):
    '''Displays the user's weapons.'''
    print("Weapons:")
    # Iterate through the user's weapons.
    for i in range(len(user.weapons)):
        # If the list index is 0, display 1.
        if i == 0:
            num = 1
        else:
            num = i + 1
        print(f"{num}. {user.weapons[i].name}")
        print("---------------------")
    choice = input("Which weapon would you like to view? ")


    # Convert the choice to an integer.
    choice = int(choice)
    # Subtract one from the choice to match the list index.
    choice = choice - 1
    # If the choice is in the range of the user's weapons, display the weapon's info.
    if choice in range(len(user.weapons)):
        display_item_details(user.weapons[choice], user)
    else:
        print("Invalid choice.")
        input("Press enter to continue.")

def display_armor(user: Player):
    '''Displays the user's armor.'''
    print("Armor:")
    for armor in user.armors:
        print(display_item_details(armor, user))
        print("----------------------------------")

def display_inventory(user: Player):
    '''Displays the user's inventory.'''
    print("Inventory:")
    for item in user.inventory:
        print(display_item_details(item, user))
        print("----------------------------------")

def display_army(user: Player):
    '''Displays the user's army.'''
    print("Army:")
    for unit in user.army:
        print(f"{unit.name}")
        print("---------------------")


def weapon_skill_calc(victor: Unit, loser: Unit):
    '''Calculates the weapon skill of the victor. Used in the battle function.'''

    # A list of exp intervals needed to reach the next weapon skill level.
    exp_required = [None, 10, 40, 100, 230, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400]

    requirement = 0
    if victor.main_hand.weapon_skill <= 20:
        requirement = exp_required[victor.main_hand.weapon_skill]

    # Compare the combat skill of the victor to the combat skill of the loser.
    if victor.combat_skill >= loser.combat_skill:
        # An exponential function is used to slightly boost the victor's weapon exp.
        difference = victor.combat_skill - loser.combat_skill
        # Make sure the difference can be used in the function.
        if difference < 0:
            difference = 1.25
        elif difference == 1:
            difference = 1.5
        victor.main_hand.exp += math.pow(difference, 1.1)
    # If the victor's combat skill is less than the loser's, the victor's weapon exp is decreased.
    else:
        victor.main_hand.exp -= math.pow(loser.combat_skill - victor.combat_skill, .9)


    if victor.main_hand.exp > requirement:
        victor.main_hand.weapon_skill += 1
        
        return True
    else:
        return False
    


skill_table = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]







# dmgdmgdmg ################
def damage_calc(base_damage: int, weapon_skill: int, quality: int, defense: int):
    '''Calculates damage.'''
    # Increase the amount of damage a weapon does by the user's weapon skill with an exponential curve.
    damage = base_damage + \
        pow(weapon_skill, 1.18)
    # Increase the amount of damage based on the quality of the weapon.
    damage = damage - pow(quality, 1.1)
    # Decrease larger amounts of damage.
    if weapon_skill > 0:
        damage = (damage - (math.log(weapon_skill) * 1.1))
    if defense > 0:
        # Create a logarithmic curve for the reduction of damage from defense.
        damage = damage - (damage * (math.log(defense)))
    # Round the damage to the nearest integer.
    damage = round(damage)
    # If the damage is somehow 0 or less, set it to 1.
    if damage <= 0:
        damage = 1
    return damage


def battle(unit_1: Unit, unit_2: Unit, user_location: Location):
    '''Battle logic.'''
    # Decides who goes first.
    unit_1_chance = random.randint(1, unit_1.combat_skill)
    unit_2_chance = random.randint(1, unit_2.combat_skill)
    # If unit_1 wins the skill check.
    if unit_1_chance > unit_2_chance:
        attacker = unit_1
        defender = unit_2

    # If unit_2 wins the skill check.
    elif unit_1_chance < unit_2_chance:
        attacker = unit_2
        defender = unit_1

    # If the skill check is a tie.
    elif unit_1_chance == unit_2_chance:
        temp = [unit_1, unit_2]
        attacker = temp.pop(random.randint(0, 1))
        defender = temp[0]
    combatants = [attacker, defender]

    # While both units are alive.
    while attacker.hp > 0 and defender.hp > 0:
        for i in range(len(combatants)):

            # Calculates whether or not the attack is blocked.
            defender_block_chance = random.randint(1, defender.combat_skill) - \
                random.randint(1, attacker.combat_skill)

            # If the attack is not blocked.
            if defender_block_chance <= 0:

                # If the defender has no armor equipped.
                if len(defender.equipped_armor) == 0:
                    defense = 0
                # If the defender has armor equipped.
                else:
                    # Calculate the total defense.
                    for armor_piece in defender.equipped_armor:
                        defense += armor_piece.defense

                # Calculate the damage.
                damage = damage_calc(
                    attacker.main_hand.base_damage, attacker.main_hand.weapon_skill, attacker.main_hand.quality, defense)
                # Subtract the damage from the defender's HP.
                defender.hp -= damage
                print(f"{defender.name} took {damage} damage.")

            # If the attack is blocked.
            else:
                print(defender.name + " blocked the attack!")

            # At the end of the action, switch the attacker and defender.
            temp = attacker
            attacker = defender
            defender = temp

            # Decide how to show the HP of the units.
            if i == 1:
                # Print the HP of both units.
                # If either unit is the user, check if the health of the user is low.
                if type(unit_1) is Player:
                    # If the user's hp is low.
                    if unit_1.hp <= 25:
                        # If the player is in the arena and their HP is less than or equal to 4.
                        if unit_1.location == Location.ARENA and unit_1.hp < 4:
                            # Set the user's HP to a random number between 1 and 3.
                            unit_1.hp = random.randint(1, 3)
                            # Print the user's HP in red.
                            unit_1.low_hp()
                            print(unit_2.hp)
                            return user_location
                        # If the player runs out of HP, they die.
                        if unit_1.hp <= 0:
                            unit_1.hp = 0
                            # If the user's location state is the arena, set their HP to a random number between 1 and 3.
                            if unit_1.location == Location.ARENA:
                                unit_1.hp = random.randint(1, 3)
                                unit_1.low_hp()
                                print(unit_2.hp)
                                return user_location

                        unit_1.low_hp()
                        print(unit_2.hp)
                    else:
                        print(unit_1.hp)
                        print(unit_2.hp)

                elif type(unit_2) is Player:
                    if unit_2.hp <= 25:
                        # If the player is in the arena and their HP is less than or equal to 4.
                        if unit_2.location == Location.ARENA and unit_2.hp < 4:
                            # Set the user's HP to a random number between 1 and 3.
                            unit_2.hp = random.randint(1, 3)
                            # Print the user's HP in red.
                            unit_2.low_hp()
                            print(unit_1.hp)
                            return user_location
                        # If the player runs out of HP, they die.
                        if unit_2.hp <= 0:
                            unit_2.hp = 0
                            unit_2.low_hp()
                            print(unit_1.hp)
                            return user_location
                        unit_2.low_hp()
                        print(unit_1.hp)
                    else:
                        print(unit_2.hp)
                        print(unit_1.hp)
                # If the player is not involved.
                else:
                    print(unit_1.hp)
                    print(unit_2.hp)
                # input("Press enter to continue.\n---")
        # If the user is dead or lost.
        # Calculate weapon skill exp.
        if type(unit_1) is Player:
            weapon_skill_calc(unit_1, unit_2)
        else:
            weapon_skill_calc(unit_2, unit_1)
        return user_location

    # If both parameters are lists, they are groups of units.
    else:
        pass

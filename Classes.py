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
    def __init__(self, name: str, weight: int, weapon_skill: int, base_damage: int, range: int, bludgeon: int, slash: int, pierce: int, poison: bool):
        self.name = name
        self.weight = weight
        self.weapon_skill = weapon_skill
        self.base_damage = base_damage
        self.range = range
        self.bludgeon = bludgeon
        self.slash = slash
        self.pierce = pierce
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
    def __init__(self, name: str, hp: int, defense: int, combat_skill: int, money: int, army: list, location: Location, carry_weight: int, weapons: list, equipped_armor: list, spare_armor: list, inventory: list, main_hand: Weapon, off_hand: Weapon, reputation: int):
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
        self.spare_armor = spare_armor
        self.inventory = inventory
        self.main_hand = main_hand
        self.off_hand = off_hand
        self.reputation = reputation

    def low_hp(self):
        '''Prints the player's hp in the color red.'''
        print(Fore.RED + str(self.hp))
        print(Style.RESET_ALL)

    def update_defense(self):
        '''Updates the player's defense.'''
        if self.equipped_armor is not None:
            temp = self.defense
            for armor in self.equipped_armor:
                temp += armor.defense
            self.defense = temp
        else:
            self.defense = 0


class Unit:
    def __init__(self, name: str, hp: int, defense: int, combat_skill: int, money: int, weapons: list, equipped_armor: list, main_hand: Weapon, off_hand: Weapon):
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


skill_table = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


def damage_calc(unit_1: Unit, unit_2: Unit, user_location: Location):
    # Decides who goes first.
    unit_1_chance = random.randint(1, unit_1.skill)
    unit_2_chance = random.randint(1, unit_2.skill)
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
        defender = temp.pop(random.randint(0, 1))
    combatants = [attacker, defender]

    # While both units are alive.
    while attacker.hp > 0 and defender.hp > 0:
        for i in range(len(combatants)):

            # Calculates whether or not the attack is blocked.
            defender_block_chance = random.randint(1, defender.skill) - \
                random.randint(1, attacker.skill)

            # If the attack is not blocked.
            if defender_block_chance <= 0:

                # If the defender has no armor equipped.
                if defender.equipped_armor is None:
                    defense = 0
                # If the defender has armor equipped.
                else:
                    # Calculate the total defense.
                    for armor_piece in defender.equipped_armor:
                        defense += armor_piece.defense

                # Increase the amount of damage a weapon does by the user's weapon skill with an exponential curve.
                damage = attacker.main_hand.base_damage + \
                    pow(attacker.main_hand.weapon_skill, 1.13)
                damage = damage * 1.15
                # Create a logarithmic curve for the reduction of damage from defense.
                damage = damage - (damage * (math.log(defense)))
                # If the damage is somehow 0 or less, set it to 1.
                if damage <= 0:
                    damage = 1
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
                input("Press enter to continue.\n---")
        # If the user is dead or lost.
        return user_location

    # If both parameters are lists, they are groups of units.
    else:
        pass

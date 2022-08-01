import random
from enum import Enum
from colorama import Fore, Style


class Location(Enum):
    TOWN = 1
    ARENA = 2
    BARRACKS = 3
    TAVERN = 4
    SHOP = 5
    STATS = 6
    QUIT = 99


class Player:
    def __init__(self, name, hp, attack, defense, skill, money, army, location, weight, inventory):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.skill = skill
        self.money = money
        self.army = army
        self.location = location
        self.weight = weight
        weight = weight
        self.inventory = inventory

    def low_hp(self):
        # Prints the player's hp in the color red.
        print(Fore.RED + str(self.hp))
        print(Style.RESET_ALL)


class Spearman:
    def __init__(self, hp, attack, defense, skill):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.skill = skill


class Knight:
    def __init__(self, hp, attack, defense, skill):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.skill = skill


class Gladiator:
    def __init__(self, name, hp, attack, defense, skill):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.skill = skill


class Food:
    def __init__(self, name, amount, hp):
        self.name = name
        self.amount = amount
        self.hp = hp


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


def battle(unit_1, unit_2, user_location):
    '''The battle logic.'''
    # If it is one-on-one combat.
    if type(unit_1) is not list and type(unit_2) is not list:
        # Decides who goes first.
        unit_1_chance = random.randint(1, unit_1.skill)
        unit_2_chance = random.randint(1, unit_2.skill)
        # If unit_1 wins the skill check.
        if unit_1_chance > unit_2_chance:
            attacker = unit_1
            defender = unit_2
            combatants = [attacker, defender]
        # If unit_2 wins the skill check.
        elif unit_1_chance < unit_2_chance:
            attacker = unit_2
            defender = unit_1
            combatants = [attacker, defender]
        # If the skill check is a tie.
        elif unit_1_chance == unit_2_chance:
            attacker = random.choice([unit_1, unit_2])
            defender = random.choice([unit_1, unit_2])
            combatants = [attacker, defender]

        # While both units are alive.
        while attacker.hp > 0 and defender.hp > 0:
            for i in range(len(combatants)):
                # Calculates initial damage based off skill and some random chance.
                damage = random.randint(1, defender.skill) - \
                    random.randint(1, attacker.skill)
                # If the initial defender took damage.
                if damage <= 0:
                    # Convert the damage to a positive number.
                    damage = abs(damage)
                    # Add the unit's weapon attack to the damage.
                    damage += attacker.attack
                    # Subtract the damage by the second unit's defense.
                    damage -= defender.defense
                    # If the damage is 0, set it to 1.
                    if damage <= 0:
                        damage = 1
                    # Subtract the damage from the first unit's hp.
                    defender.hp -= damage
                    print(
                        f"{defender.name} took {abs(damage)} damage.")
                    # At the end of the turn, switch the attacker and defender.
                    # if i == 1:
                    # Switch the attacker and defender for next turn.
                    temp = attacker
                    attacker = defender
                    defender = temp

                # If the attack was blocked.
                else:
                    print(defender.name + " blocked the attack!")
                    # At the end of the action, switch the attacker and defender.
                    temp = attacker
                    attacker = defender
                    defender = temp

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

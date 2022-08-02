import math
from typing import Any
import random


weapon_attack = 20
weapon_skill = 10
defense = 1.15


# # Increase the amount of damage a weapon does by the user's weapon skill with an exponential curve.
# damage = weapon_attack + pow(weapon_skill, 1.25)
# damage = damage * 1.15
# # Create a logarithmic curve for the reduction of damage from defense.
# damage = damage - (damage * (math.log(defense)))
# # If the damage is somehow 0 or less, set it to 1.
# if damage <= 0:
#     damage = 1
# print(str(weapon_skill) + " skill and " + str(weapon_attack) +
#       " attack = " + str(round(damage)) + " damage")


defender_block_chance = {
    "defender": random.randint(1, 20)}
attacker_block_chance = {
    "attacker": random.randint(1, 20)}
block_chance = [defender_block_chance, attacker_block_chance]
block_chance = block_chance.sort(key=)
print(block_chance)

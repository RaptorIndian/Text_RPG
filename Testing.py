import math
import random
from weapons import *

from classes import *

name = "Greg"
hp = 100
defense = 0
combat_skill = 10
money = 50
army = []
carry_weight = 30
weapons = []
equipped_armor = []
spare_armor = []
inventory = []
main_hand = steel_sword
main_hand.weapon_skill = 2
off_hand = None
reputation = 0
user = Player(name, hp, defense, combat_skill, money, army, Location.TOWN, carry_weight,
                  weapons, equipped_armor, spare_armor, inventory, main_hand, off_hand, reputation)

name = "Poly"
hp = 100
defense = 0
combat_skill = 1
money = 50
weapons = []
equipped_armor = []
main_hand = fists
off_hand = None
soldier = Unit(name, hp, defense, combat_skill, money, weapons, equipped_armor, main_hand, off_hand)

loop = True
while loop:
    battle(user, soldier, Location.ARENA)
    if user.hp <= 0 or soldier.hp <= 0:
        # heal
        user.hp = 100
        soldier.hp = 100
    print(user.main_hand.weapon_skill)

print(user.main_hand.exp)

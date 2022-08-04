import math
import random
from weapons import *

from classes import *

name = "Greg"
hp = 100
defense = 0
combat_skill = 1
money = 50
army = []
carry_weight = 30
weapons = []
equipped_armor = []
spare_armor = []
inventory = []
main_hand = fists
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


for i in range(21):
    count = 0
    calc = False
    if i > 0:
        user.main_hand.weapon_skill = i
        while calc == False:
            count += 1
            calc = weapon_skill_calc(user, soldier)
            print(str(i) + " " + str(calc) + " " + str(count))

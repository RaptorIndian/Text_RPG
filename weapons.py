
from classes import *

kills_required = [10]

# For higher damage, reduce quality and increase weapon skill.
name = "Fists"
description = "Good for punching."
price = 0
weight = 0
weapon_skill = 1
base_damage = 10
reach = 0
bludgeon = 1
slash = 0
pierce = 0
quality = .25

fists = Weapon(name, description, price, weight, weapon_skill, base_damage,
                      reach, bludgeon, slash, pierce, quality)

name = "Copper Sword"
description = "A simple sword made of copper. High chance to do slashing damage, moderately good chance to do piercing damage, and almost no chance to do bludgeoning damage."
price = 350
weight = 9
weapon_skill = 1
base_damage = 10
reach = 1
bludgeon = 1
slash = 6
pierce = 3
quality = .2

copper_sword = Weapon(name, description, price, weight, weapon_skill, base_damage,
                      reach, bludgeon, slash, pierce, quality)


name = "Bronze Sword"
weight = 10
weapon_skill = 1
base_damage = 13
reach = 1
bludgeon = 1
slash = 6
pierce = 3
quality = .15

bronze_sword = Weapon(name, description, price, weight, weapon_skill, base_damage,
                      reach, bludgeon, slash, pierce, quality)


name = "Iron Sword"
weight = 12
weapon_skill = 1
base_damage = 15
reach = 1
bludgeon = 1
slash = 6
pierce = 3
quality = .1

iron_sword = Weapon(name, description, price, weight, weapon_skill, base_damage,
                      reach, bludgeon, slash, pierce, quality)


name = "Steel Sword"
weight = 14
weapon_skill = 1
base_damage = 17
reach = 1
bludgeon = 1
slash = 16
pierce = 3
quality = .05

steel_sword = Weapon(name, description, price, weight, weapon_skill, base_damage,
                      reach, bludgeon, slash, pierce, quality)

swords = [copper_sword, bronze_sword, iron_sword, steel_sword]


name = " Copper Axe"
weight = 12
weapon_skill = 1
base_damage = 10
reach = 1
bludgeon = 2
slash = 8
pierce = 0
quality = .75

copper_axe = Weapon(name, description, price, weight, weapon_skill, base_damage,
                      reach, bludgeon, slash, pierce, quality)



name = "Bronze Axe"
weight = 13
weapon_skill = 1
base_damage = 10
reach = 1
bludgeon = 2
slash = 8
pierce = 0
quality = .73

bronze_axe = Weapon(name, description, price, weight, weapon_skill, base_damage,
                      reach, bludgeon, slash, pierce, quality)


name = "Iron Axe"
weight = 15
weapon_skill = 1
base_damage = 10
reach = 1
bludgeon = 2
slash = 8
pierce = 0
quality = .7

iron_axe = Weapon(name, description, price, weight, weapon_skill, base_damage,
                      reach, bludgeon, slash, pierce, quality)


name = "Steel Axe"
weight = 16
weapon_skill = 1
reach = 1
bludgeon = 2
slash = 8
pierce = 0
quality = .66

steel_axe = Weapon(name, description, price, weight, weapon_skill, base_damage,
                      reach, bludgeon, slash, pierce, quality)

axes = [copper_axe, bronze_axe, iron_axe, steel_axe]


name = "Copper Mace"
weight = 10
weapon_skill = 1
base_damage = 10
reach = 1
bludgeon = 7
slash = 0
pierce = 3
quality = .75

copper_mace = Weapon(name, description, price, weight, weapon_skill, base_damage,
                      reach, bludgeon, slash, pierce, quality)


name = "Bronze Mace"
weight = 11
weapon_skill = 1
base_damage = 10
reach = 1
bludgeon = 7
slash = 0
pierce = 3
quality = .73

bronze_mace = Weapon(name, description, price, weight, weapon_skill, base_damage,
                      reach, bludgeon, slash, pierce, quality)


name = "Iron Mace"
weight = 13
weapon_skill = 1
base_damage = 10
reach = 1
bludgeon = 7
slash = 0
pierce = 3
quality = .7

iron_mace = Weapon(name, description, price, weight, weapon_skill, base_damage,
                      reach, bludgeon, slash, pierce, quality)


name = "Steel Mace"
weight = 15
weapon_skill = 1
base_damage = 10
reach = 1
bludgeon = 7
slash = 0
pierce = 3
quality = .66

steel_mace = Weapon(name, description, price, weight, weapon_skill, base_damage,
                      reach, bludgeon, slash, pierce, quality)

maces = [copper_mace, bronze_mace, iron_mace, steel_mace]

name = "Copper Spear"
weight = 13
weapon_skill = 1
base_damage = 10
reach = 2
bludgeon = 3
slash = 0
pierce = 7
quality = .75

copper_spear = Weapon(name, description, price, weight, weapon_skill, base_damage,
                      reach, bludgeon, slash, pierce, quality)


name = "Bronze Spear"
weight = 14
weapon_skill = 1
base_damage = 10
reach = 2
bludgeon = 3
slash = 0
pierce = 7
quality = .73

bronze_spear = Weapon(name, description, price, weight, weapon_skill, base_damage,
                      reach, bludgeon, slash, pierce, quality)


name = "Iron Spear"
weight = 16
weapon_skill = 1
base_damage = 10
reach = 2
bludgeon = 3
slash = 0
pierce = 7
quality = .7

iron_spear = Weapon(name, description, price, weight, weapon_skill, base_damage,
                      reach, bludgeon, slash, pierce, quality)


name = "Steel Spear"
weight = 18
weapon_skill = 1
base_damage = 10
reach = 2
bludgeon = 3
slash = 0
pierce = 7
quality = .66

steel_spear = Weapon(name, description, price, weight, weapon_skill, base_damage,
                      reach, bludgeon, slash, pierce, quality)

spears = [copper_spear, bronze_spear, iron_spear, steel_spear]


name = "Copper Dagger"
weight = 5
weapon_skill = 1
base_damage = 5
reach = 1
bludgeon = 0
slash = 3
pierce = 7
quality = .75
poison = True


copper_dagger = Weapon(name, description, weight, weapon_skill, base_damage,
                      reach, bludgeon, slash, pierce, quality, poison)


name = "Bronze Dagger"
weight = 6
weapon_skill = 1
base_damage = 5
reach = 1
bludgeon = 0
slash = 3
pierce = 7
quality = .73
poison = True

bronze_dagger = Weapon(name, description, weight, weapon_skill, base_damage,
                      reach, bludgeon, slash, pierce, quality, poison)


name = "Iron Dagger"
weight = 7
weapon_skill = 1
base_damage = 5
reach = 1
bludgeon = 0
slash = 3
pierce = 7
quality = .7
poison = True

iron_dagger = Weapon(name, description, weight, weapon_skill, base_damage,
                      reach, bludgeon, slash, pierce, quality, poison)


name = "Steel Dagger"
weight = 8
weapon_skill = 1
base_damage = 5
reach = 1
bludgeon = 0
slash = 3
pierce = 7
quality = .66
poison = True

steel_dagger = Weapon(name, description, weight, weapon_skill, base_damage,
                      reach, bludgeon, slash, pierce, quality, poison)

daggers = [copper_dagger, bronze_dagger, iron_dagger, steel_dagger]

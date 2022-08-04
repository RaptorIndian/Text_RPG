
from classes import *

name = "Fists"
weight = 0
weapon_skill = 0
base_damage = 2
reach = 0
bludgeon = 1
slash = 0
pierce = 0
quality = 1

fists = Weapon(name, weight, weapon_skill, base_damage,
               reach, bludgeon, slash, pierce, quality)

name = "Copper Sword"
weight = 9
weapon_skill = 0
base_damage = 10
reach = 1
bludgeon = 1
slash = 6
pierce = 3
quality = .94


copper_sword = Weapon(name, weight, weapon_skill, base_damage,
                      reach, bludgeon, slash, pierce, quality)


name = "Bronze Sword"
weight = 10
weapon_skill = 0
base_damage = 10
reach = 1
bludgeon = 1
slash = 6
pierce = 3
quality = .98

bronze_sword = Weapon(name, weight, weapon_skill, base_damage,
                      reach, bludgeon, slash, pierce, quality)


name = "Iron Sword"
weight = 12
weapon_skill = 0
base_damage = 10
reach = 1
bludgeon = 1
slash = 6
pierce = 3
quality = 1.02

iron_sword = Weapon(name, weight, weapon_skill, base_damage,
                    reach, bludgeon, slash, pierce, quality)


name = "Steel Sword"
weight = 14
weapon_skill = 0
base_damage = 10
reach = 1
bludgeon = 1
slash = 16
pierce = 3
quality = 1.073

steel_sword = Weapon(name, weight, weapon_skill, base_damage,
                     reach, bludgeon, slash, pierce, quality)

swords = [copper_sword, bronze_sword, iron_sword, steel_sword]


name = " Copper Axe"
weight = 12
weapon_skill = 0
base_damage = 10
reach = 1
bludgeon = 2
slash = 8
pierce = 0
quality = .94

copper_axe = Weapon(name, weight, weapon_skill, base_damage,
                    reach, bludgeon, slash, pierce, quality)


name = "Bronze Axe"
weight = 13
weapon_skill = 0
base_damage = 10
reach = 1
bludgeon = 2
slash = 8
pierce = 0
quality = .98

bronze_axe = Weapon(name, weight, weapon_skill, base_damage,
                    reach, bludgeon, slash, pierce, quality)


name = "Iron Axe"
weight = 15
weapon_skill = 0
base_damage = 10
reach = 1
bludgeon = 2
slash = 8
pierce = 0
quality = 1.02

iron_axe = Weapon(name, weight, weapon_skill, base_damage,
                  reach, bludgeon, slash, pierce, quality)


name = "Steel Axe"
weight = 16
weapon_skill = 0
reach = 1
bludgeon = 2
slash = 8
pierce = 0
quality = 1.073

steel_axe = Weapon(name, weight, weapon_skill, base_damage,
                   reach, bludgeon, slash, pierce, quality)

axes = [copper_axe, bronze_axe, iron_axe, steel_axe]


name = "Copper Mace"
weight = 10
weapon_skill = 0
base_damage = 10
reach = 1
bludgeon = 7
slash = 0
pierce = 3
quality = .94

copper_mace = Weapon(name, weight, weapon_skill, base_damage, reach,
                     bludgeon, slash, pierce, quality)


name = "Bronze Mace"
weight = 11
weapon_skill = 0
base_damage = 10
reach = 1
bludgeon = 7
slash = 0
pierce = 3
quality = .98

bronze_mace = Weapon(name, weight, weapon_skill, base_damage, reach,
                     bludgeon, slash, pierce, quality)


name = "Iron Mace"
weight = 13
weapon_skill = 0
base_damage = 10
reach = 1
bludgeon = 7
slash = 0
pierce = 3
quality = 1.02

iron_mace = Weapon(name, weight, weapon_skill, base_damage, reach,
                   bludgeon, slash, pierce, quality)


name = "Steel Mace"
weight = 15
weapon_skill = 0
base_damage = 10
reach = 1
bludgeon = 7
slash = 0
pierce = 3
quality = 1.073

steel_mace = Weapon(name, weight, weapon_skill, base_damage, reach,
                    bludgeon, slash, pierce, quality)

maces = [copper_mace, bronze_mace, iron_mace, steel_mace]

name = "Copper Spear"
weight = 13
weapon_skill = 0
base_damage = 10
reach = 2
bludgeon = 3
slash = 0
pierce = 7

copper_spear = Weapon(name, weight, weapon_skill, base_damage, reach,
                     bludgeon, slash, pierce, quality)


name = "Bronze Spear"
weight = 14
weapon_skill = 0
base_damage = 10
reach = 2
bludgeon = 3
slash = 0
pierce = 7
quality = .98

bronze_spear = Weapon(name, weight, weapon_skill, base_damage, reach,
                      bludgeon, slash, pierce, quality)


name = "Iron Spear"
weight = 16
weapon_skill = 0
base_damage = 10
reach = 2
bludgeon = 3
slash = 0
pierce = 7
quality = 1.02

iron_spear = Weapon(name, weight, weapon_skill, base_damage, reach,
                    bludgeon, slash, pierce, quality)


name = "Steel Spear"
weight = 18
weapon_skill = 0
base_damage = 10
reach = 2
bludgeon = 3
slash = 0
pierce = 7
quality = 1.073

steel_spear = Weapon(name, weight, weapon_skill, base_damage, reach,
                     bludgeon, slash, pierce, quality)

spears = [copper_spear, bronze_spear, iron_spear, steel_spear]


name = "Copper Dagger"
weight = 5
weapon_skill = 0
base_damage = 5
reach = 1
bludgeon = 0
slash = 3
pierce = 7
quality = .84
poison = True


copper_dagger = Weapon(name, weight, weapon_skill, base_damage, reach,
                       bludgeon, slash, pierce, quality, poison)


name = "Bronze Dagger"
weight = 6
weapon_skill = 0
base_damage = 5
reach = 1
bludgeon = 0
slash = 3
pierce = 7
quality = .86
poison = True

bronze_dagger = Weapon(name, weight, weapon_skill, base_damage, reach,
                       bludgeon, slash, pierce, quality, poison)


name = "Iron Dagger"
weight = 7
weapon_skill = 0
base_damage = 5
reach = 1
bludgeon = 0
slash = 3
pierce = 7
quality = .88
poison = True

iron_dagger = Weapon(name, weight, weapon_skill, base_damage, reach,
                     bludgeon, slash, pierce, quality, poison)


name = "Steel Dagger"
weight = 8
weapon_skill = 0
base_damage = 5
reach = 1
bludgeon = 0
slash = 3
pierce = 7
quality = .89
poison = True

steel_dagger = Weapon(name, weight, weapon_skill, base_damage, reach,
                      bludgeon, slash, pierce, quality, poison)

daggers = [copper_dagger, bronze_dagger, iron_dagger, steel_dagger]


def damage_calc_test(base_damage: int, weapon_skill: int, quality: int, defense: int):
    '''Calculates damage.'''
    # Increase the amount of damage a weapon does by the user's weapon skill with an exponential curve.
    damage = base_damage + \
        pow(weapon_skill, quality)

    if weapon_skill < 10:
        # Increase the amount of damage based on the quality of the weapon.
        damage = (damage - pow(quality, 1.2)) * quality
    elif weapon_skill >= 10:
        damage = (damage - pow(quality, 1.23)) * quality
    elif weapon_skill >= 20:
        damage = (damage - pow(quality, 1.26)) * quality

    # Decrease the amount of damage based on the defense of the enemy.
    if defense > 0:
        # Create a logarithmic curve for the reduction of damage from defense.
        damage = damage - (damage * (math.log(defense)))

    # Round the damage to the nearest integer.
    damage = round(damage)

    # If the damage is somehow 0 or less, set it to 1.
    if damage <= 0:
        damage = 1

    return damage


for axe in daggers:
    print(axe.name)
    for i in range(31):
        # Calculate the damage each weapon will do against an enemy.
        if i > 0:
            print(damage_calc_test(axe.base_damage, i, axe.quality, 0))

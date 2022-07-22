import random


class Player:
    def __init__(self, name, hp, attack, defense, skill, money, army):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.skill = skill
        self.money = money
        self.army = army

    army = []

    def take_damage(self, enemy_attack, enemy_skill):
        damage = random.randint(1, self.skill) - random.randint(1, enemy_skill)
        if damage < 0:
            damage = abs(damage)
            damage += enemy_attack
            damage -= self.defense
            self.hp -= damage
            print("You took {} damage.".format(
                enemy_attack - self.defense - damage))
        else:
            print(self.name + " blocked the attack!")


class Spearman:
    def __init__(self, hp, attack, defense, skill):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.skill = skill

    def take_damage(self, enemy_attack, enemy_skill):
        skill_check = self.skill/enemy_skill
        if skill_check > 0.5:
            self.hp -= enemy_attack - self.defense


class Knight:
    def __init__(self, hp, attack, defense, skill):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.skill = skill

    def take_damage(self, enemy_attack, enemy_skill):
        skill_check = self.skill/enemy_skill
        if skill_check > 0.5:
            self.hp -= enemy_attack - self.defense


class Gladiator:
    def __init__(self, name, hp, attack, defense, skill):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.skill = skill

    def take_damage(self, enemy_attack, enemy_skill):
        damage = random.randint(1, self.skill) - random.randint(1, enemy_skill)
        if damage < 0:
            damage = abs(damage)
            damage += enemy_attack
            damage -= self.defense
            self.hp -= damage
            print("You took {} damage.".format(
                enemy_attack - self.defense - damage))
        else:
            print(self.name + " blocked the attack!")

from Classes import *
from Main import user
from Town import town_loop


def arena():
    loop = True
    while loop == True:
        print("You enter the arena.\n")
        print("You can battle against others or train yourself.\n")
        print("1. Battle\n")
        print("2. Train\n")
        print("3. Go back\n")
        arena_choice = input("Enter your choice: ")
        if arena_choice == "1":
            # If the user chose to battle, create a gladiator.
            gladiator = Gladiator("The gladiator", 100, 10, 10, 30)
            # The battle logic.
            while gladiator.hp > 0 and user.hp > 0:
                # The person who attacks first is determined by using their skill levels in a random range, and the higher number chosen is the first attacker.
                if random.randint(1, gladiator.skill) > random.randint(1, user.skill):
                    # The gladiator attacks first.
                    user.take_damage(gladiator.attack, gladiator.skill)
                    # If the user's HP is greater than 0, the user attacks.
                    if user.hp > 0:
                        # The user attacks.
                        gladiator.take_damage(user.attack, user.skill)
                elif random.randint(1, gladiator.skill) < random.randint(1, user.skill):
                    # The user attacks first.
                    gladiator.take_damage(user.attack, user.skill)
                    # If the gladiator's HP is greater than 0, the gladiator attacks.
                    if gladiator.hp > 0:
                        # The gladiator attacks.
                        user.take_damage(gladiator.attack, gladiator.skill)
                print(user.hp, gladiator.hp)
                input("Press enter to continue.\n")
            # Depending on the outcome of the battle, print the results.
            if gladiator.hp <= 0:
                print("You won the battle!\n")
                town_loop()
            elif user.hp <= 0:
                print("You lost the battle!\n")
                town_loop()

        elif arena_choice == "2":
            pass
        elif arena_choice == "3":
            town_loop()

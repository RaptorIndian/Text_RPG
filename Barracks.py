from classes import *


def do_barracks(user: Player):
    print("---------------------\n")
    print("There is a large number of soldiers waiting in the barracks just waiting to be recruited.\n")
    print("You can also train or purchase arrows.\n")
    print("1. Recruit a soldier")
    print("2. Train yourself")
    print("3. Buy arrows")
    barracks_choice = input("Enter your choice: ")
    print("---------------------\n")

    # If the user chose to recruit a soldier, ask which type of soldier they want to recruit.
    if barracks_choice == "1":
        print("Who will you recruit?\n---------------------\n")
        print("1. Spearman\n")
        print("2. Knight\n")
        print("3. Go back\n")
        # Request user input.
        recruitment_choice = input("Enter your choice: ")
        # If the user chose to recruit a spearman, ask how many.
        amount = int(input("How many: "))
        # Add the amount of spearmen to the user's army with the default stats.
        if amount > 0:
            hp = int(100)
            attack = int(30)
            defense = int(20)
            skill = int(10)
            for i in range(amount):
                user.army.append(
                    Spearman(hp, attack, defense, skill))

        # If the user chose to recruit a spearman, ask how many.
        elif recruitment_choice == "1":
            amount = int(input("How many: "))
            # Add the amount of knights to the user's army with the default stats.
            if amount > 0:
                hp = int(100)
                attack = int(50)
                defense = int(45)
                skill = int(30)
                for i in range(amount):
                    user.army.append(Spearman(hp, attack, defense, skill))

        # If the user chose to recruit a knight, ask how many.
        elif recruitment_choice == "2":
            amount = int(input("How many: "))
            # Add the amount of knights to the user's army with the default stats.
            if amount > 0:
                hp = int(100)
                attack = int(50)
                defense = int(45)
                skill = int(30)
                for i in range(amount):
                    user.army.append(Spearman(hp, attack, defense, skill))

        elif recruitment_choice == "3":
            # Return the user to the barracks menu.
            pass

    # If the user chose to train.
    if barracks_choice == "2":
        print(
            "You begin training. Your stats have a chance to increase the more you train.\n")
        # The training logic.
        if user.hp <= 25:
            print("You are too injured to train.\n")
            # Return the user to the barracks menu.
            return Location.BARRACKS
        else:
            # There is a random chance that the stats will increase.
            health_lost = random.randint(10, 25)

            for interval in skill_table:
                # If the user's skill is less than 10.
                if user.skill < interval:
                    # The chance to gain skill is 1/8.
                    if random.randint(1, 6) == 1:
                        # Increase the user's skill by a random number between 1 and 2.
                        user.skill += random.randint(1, 2)
                else:
                    # The chance to gain skill is 1/12.
                    if random.randint(1, 10) == 1:
                        # Increase the user's skill by a random number between 1 and 2.
                        skill_increase = random.randint(1, 2)
                        user.skill += skill_increase

                # Calculate how much health the user will lose next.
                health_lost = random.randint(10, 25)

                # If the user's health is less than the health that will be lost, cancel.
                if user.hp - health_lost <= 0:
                    print(
                        "You feel too injured to continue training, you don't feel any more skillful than you were before.\n")
                    # Return the user to the barracks menu.
                    return Location.BARRACKS
                else:
                    # Subtract the health lost from the user's hp.
                    user.hp -= health_lost
                input("Press enter to continue training.\n")

            # If they did not gain any skill.
            if skill_increase is not None:
                print(f"Your skill has increased by {skill_increase}.")
                skill_increase = None

            else:
                print(
                    "You feel too injured to continue training, you don't feel any more skillful than you were before.\n")
                input("Press enter to continue.\n")
                # Return the user to the barracks menu.
                return Location.BARRACKS

    # # If the user chose to buy arrows.
    # if barracks_choice == "3":
    #     print("You can buy arrows here.\n")
    #     # Request user input.
    #     amount = int(input("How many: "))
    #     # If the user has enough money.
    #     if user.money >= amount * 10:
    #         # Subtract the money from the user's money.
    #         user.money -= amount * 10
    #         # Add the amount of arrows to the user's inventory.
    #         user.inventory.append(Arrow(amount))
    #     else:
    #         print("You do not have enough money.\n")
    #         # Return the user to the barracks menu.
    #         return Location.BARRACKS

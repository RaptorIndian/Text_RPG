from classes import *


def do_barracks(user: Player):
    print("There is a large number of soldiers waiting in the barracks just waiting to be recruited.\n")

    print("Who will you recruit?\n---------------------\n")
    print("1. Spearman\n")
    print("2. Knight\n")
    print("3. Go back\n")
    # Request user input.
    barracks_choice = input("Enter your choice: ")
    # If the user chose to recruit a spearman, ask how many.
    if barracks_choice == "1":
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

    # If the user chose to recruit a knight, ask how many.
    elif barracks_choice == "2":
        amount = int(input("How many: "))
        # Add the amount of knights to the user's army with the default stats.
        if amount > 0:
            hp = int(100)
            attack = int(50)
            defense = int(45)
            skill = int(30)
            for i in range(amount):
                user.army.append(Knight(hp, attack, defense, skill))
    elif barracks_choice == "3":
        return Location.TOWN

    return Location.BARRACKS

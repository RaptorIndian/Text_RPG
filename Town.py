from Classes import *
from Main import user
from Town import town_loop
from Barracks import barracks
from Tavern import tavern


def town_loop():
    loop = True
    while loop == True:
        print("What would you like to do?\n---------------------\n")
        print("1. Go to the barracks\n")
        print("2. Go to the tavern\n")
        print("3. Go to the arena\n")
        print("4. Check your stats\n")
        choice = input("Enter your choice: ")

        if choice == "1":
            barracks()

        elif choice == "2":
            tavern()

        elif choice == "3":
            arena()

        elif choice == "4":
            print(user.name)
            print("---------------------\n")
            print(f"You have $" + str(user.money) + ".\n")
            print(f"Your HP is " + str(user.hp) + ".\n")
            print(f"Your attack is " + str(user.attack) + ".\n")
            print(f"Your defense is " + str(user.defense) + ".\n")
            print(f"Your skill is " + str(user.skill) + ".\n")

            units = [soldier.__class__.__name__ for soldier in user.army]
            spear_amount = units.count("Spearman")
            knight_amount = units.count("Knight")
            final_amount = ""
            if spear_amount > 0:
                final_amount += f"\n{spear_amount} Spearman(s) "
            if knight_amount > 0:
                final_amount += f"\n{knight_amount} Knight(s) "
            print(
                f"Your army consists of {len(user.army)} units. {final_amount}\n")
            input("Press enter to continue.\n")
            town_loop()

        # Check the overall health of the army.


main_loop = True
while main_loop == True:
    town_loop()

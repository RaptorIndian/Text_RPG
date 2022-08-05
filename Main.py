from classes import *
from barracks import do_barracks
from town import do_town
from arena import do_arena
from tavern import do_tavern
from shop import do_shop
from stats import do_stats

# The game runs from this file.


def main():
    # The user will create a character upon startup.
    name = input("What will the name of your character be?\n").title()
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
    main_hand = Weapon("Fists", 0, 1, 3, 0, 0, 0, 0, False)
    off_hand = None
    reputation = 0
    # Creates a player object with the name and default stats of the character.
    user = Player(name, hp, defense, combat_skill, money, army, Location.TOWN, carry_weight,
                  weapons, equipped_armor, spare_armor, inventory, main_hand, off_hand, reputation)

    # Give the user the option to visit the barracks, the tavern, or the arena.
    print("You wake up one day in your home town of Argford. You decide today to do something with your life.\n")
    print("You can go to the barracks to train your character, you can go to the arena to fight, and a tavern to rest.\n")
    print("You can also go to the shop near the town sqaure.\n")

    # Playing state.
    playing = True
    while playing:
        print("---------------------")
        if user.location == Location.TOWN:
            user.location = do_town(user)

        elif user.location == Location.ARENA:
            user.location = do_arena(user)

        elif user.location == Location.BARRACKS:
            user.location = do_barracks(user)

        elif user.location == Location.SHOP:
            user.location = do_shop(user)

        elif user.location == Location.TAVERN:
            user.location = do_tavern(user)

        elif user.location == Location.STATS:
            location_name = "Green Town"
            user.location = do_stats(user, location_name)

        elif user.location == Location.QUIT:
            playing = False
            print("You quit the game.")
            break


main()

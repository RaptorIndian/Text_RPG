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
    # Creates a player object with the name and default stats of the character.
    current_location = Location.TOWN
    user = Player(name, 100, 10, 0, 5, 0, [], current_location, 0, [])
    user.money = 100

    # Give the user the option to visit the barracks, the tavern, or the arena.
    print("You wake up one day in your home town of Argford. You decide today to start on a journey.\n")
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

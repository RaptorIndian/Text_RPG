from classes import *
from barracks import do_barracks
from town import do_town
from arena import do_arena


def main():
    # The user will create a character upon startup.
    name = input("What will the name of your character be?\n").title()
    # Creates a player object with the name and default stats of the character.
    current_location = Location.TOWN
    user = Player(name, 100, 10, 0, 5, 0, [], current_location)

    # Give the user the option to visit the barracks, the tavern, or the arena.
    print("You wake up one day in your home town of Argford. You decide today to start on a journey.\n")
    print("You can go to the barracks to train your character or you can go to the arena to fight.\n")
    print("You can also go to the tavern to rest.\n")

    playing = True
    while playing:
        if user.location == Location.TOWN:
            user.location = do_town(user)

        elif user.location == Location.ARENA:
            user.location = do_arena(user)

        elif current_location == Location.BARRACKS:
            user.location = do_barracks(user)
        else:
            # No location
            pass


main()

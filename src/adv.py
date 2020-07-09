from room import Room
from player import Player
from item import Item
from format_text import format_text
import sys
import os
import platform

# Declare all the rooms
rooms = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons",
                    [
                        Item(
                            "Moldy stick",
                            "It's seen better days, but it has a sharp tip that could prove useful in combat."
                        ),
                        Item(
                            "Cow pie",
                            "You really don't want to pick this up"
                        )
                    ]
                    ),

    'foyer': Room("Foyer",
                  """
                  Dim light filters in from the south. Dusty
                  passages run north and east.
                  """
                  ),

    'overlook': Room("Grand Overlook",
                     """
                     A steep cliff appears before you, falling
                     into the darkness. Ahead to the north, a light flickers
                     in the distance, but there is no way across the chasm.
                     """
                     ),

    'narrow': Room("Narrow Passage",
                   """
                   The narrow passage bends here from west
                   to north. The smell of gold permeates the air.
                   """
                   ),

    'treasure': Room("Treasure Chamber",
                     """
                     You've found the long-lost treasure
                     chamber! Sadly, it has already been completely emptied
                     by earlier adventurers. The only exit is to the south.
                     """
                     ),
}


# Link rooms together
rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']

# Helper code for main loop


def clear():
    if platform.system() is 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def print_err(text):
    print(f"\033[91m{text}\033[00m")


instructions = ("What would you like to do?\n"
                "You can travel (n)orth, (s)outh, (e)ast, or (w)est.\n"
                "You can (l)oot the room or open your (i)nventory.\n"
                "You can (q)uit the game.\n")

# Make a new player object that is currently in the 'outside' room.
player = Player(location=rooms['outside'])
directions = ["n", "s", "e", "w"]

# Initialize
clear()

# Main loop
while True:
    print(player.location, "\n")
    player_input = input(instructions)
    print("\033[F                                         ")

    if player_input is "q":
        print("Goodbye!")
        sys.exit(0)

    elif player_input in directions:
        new_room = player.location.move(player_input)
        clear()
        if new_room is None:
            print_err("You cannot move in that direction!\n")
        else:
            player.location = new_room

    elif player_input is "l":
        print(player.location.items)
        looting_input = input("\nPick up an item with 'get [item_name]'.\n"
                              "You can also (s)top looting.\n")

        while (looting_input is not "s"
               and len(player.location.items) > 0):

            if not looting_input.lower().startswith("get"):
                print("I didn't understand that.\n")

            else:
                item_name = " ".join(looting_input.split(" ")[1:])
                looted_item = player.location.items.remove(item_name)

                if looted_item is None:
                    print(f"Sorry, this room doesn't contain a(n) {item_name}")
                else:
                    player.items.add(looted_item)
                    print(f"You picked up the {item_name}")
            looting_input = input("You can continue looting or (s)top.\n")
        clear()
        print(f"You finished looting the {player.location.name}")

    else:
        clear()
        print_err("Command not recognized.\n")

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

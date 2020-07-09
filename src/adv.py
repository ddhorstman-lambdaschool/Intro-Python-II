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
                    "North of you, the cave mount beckons"
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

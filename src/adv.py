from room import Room
from player import Player
import sys
import os
import platform

# Declare all the rooms
rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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


def clear():
    if platform.system() is 'Windows':
        os.system('cls')
    else:
        os.system('clear')


# Make a new player object that is currently in the 'outside' room.
player = Player(location='outside')
room = rooms[player.location]
clear()
# Write a loop that:
while True:

    print(room, "\n")
    player_input = input(
        "Would you like to travel (n)orth, (s)outh, (e)ast, or (w)est?\nYou can also (q)uit at any time.\n")

    if player_input is "q":
        print("Goodbye!")
        sys.exit(0)

    new_room = room.move(player_input)
    if not new_room:
        clear()
        print("Error: Cannot move in that direction\n")
        continue

    room = new_room

    clear()


# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

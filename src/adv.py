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


def print_confirmation(text):
    print(f"\033[92m{text}\033[00m")


def print_emphasis(text):
    print(f"\033[96m\033[04m{text}\033[00m")


def clear_prev_line():
    print("\033[F                                                  \033[F")


instructions = (
    "You can travel (n)orth, (s)outh, (e)ast, or (w)est.\n"
    "You can (l)oot the room or open your (i)nventory.\n"
    "You can (q)uit the game.\n"
)

# Make a new player object that is currently in the 'outside' room.
player = Player(location=rooms['outside'], items=[
                Item("Lunch", "A very soggy PB&J sandwich")])
directions = ["n", "s", "e", "w"]

# Initialize
clear()

# Main loop
while True:
    print(player.location, "\n")
    print_emphasis("What would you like to do?")
    player_input = input(instructions)
    clear_prev_line()

    if player_input is "q":
        print("Goodbye!")
        sys.exit(0)

    elif player_input in directions:
        new_room = player.location.move(player_input)
        clear()
        if new_room is None:
            print_err("You cannot move in that direction!\n")
        else:
            print_confirmation(f"You moved to the {new_room.name}\n")
            player.location = new_room

    elif player_input is "i":
        if len(player.items) is 0:
            clear()
            print_err("Your inventory is empty\n")
            continue
        print_emphasis("Inventory:")
        print(player.items)
        item_input = input("\nDrop an item with 'drop [item_name]'.\n"
                           "You can also go (b)ack.\n")
        clear_prev_line()
        while (item_input is not "b"
                and len(player.items) > 0):

            if not item_input.lower().startswith("drop"):
                print("I didn't understand that.")

            else:
                item_name = " ".join(item_input.split(" ")[1:])
                moved_item = player.items.remove(item_name)

                if moved_item is None:
                    print(f"Sorry, you don't have {item_name}")
                else:
                    player.location.items.add(moved_item)
                    print(f"You dropped the {item_name}")
                    if len(player.items) is 0:
                        continue
            item_input = input(
                "You can continue 'drop'-ping items or go (b)ack.\n")
            clear_prev_line()
        clear()
        print_confirmation(f"You closed your inventory\n")

    elif player_input is "l":
        if len(player.location.items) is 0:
            clear()
            print_err(f"There are no items in the {player.location.name}\n")
            continue
        print_emphasis("Room contents:")
        print(player.location.items)
        item_input = input("\nPick up an item with 'get [item_name]'.\n"
                           "You can also go (b)ack.\n")
        clear_prev_line()

        while (item_input is not "b"
                and len(player.location.items) > 0):

            if not item_input.lower().startswith("get"):
                print("I didn't understand that.")

            else:
                item_name = " ".join(item_input.split(" ")[1:])
                moved_item = player.location.items.remove(item_name)

                if moved_item is None:
                    print(f"Sorry, this room doesn't contain {item_name}")
                else:
                    player.items.add(moved_item)
                    print(f"You picked up the {item_name}")
                    if len(player.location.items) is 0:
                        continue
            item_input = input(
                "You can continue 'get'-ting items or go (b)ack.\n")
            clear_prev_line()
        clear()
        print_confirmation(
            f"You finished looting the {player.location.name}\n")

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

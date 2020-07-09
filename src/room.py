# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap
import shutil
from format_text import format_text


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return (format_text(f"You are standing in the {self.name}")
                + "\n"
                + format_text(self.description)
                + "\n")

    def move(self, direction):
        try:
            return getattr(self, f"{direction}_to")
        except AttributeError:
            #print (f"Error: No room found for direction '{direction}'")
            return None

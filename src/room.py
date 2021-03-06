
from format_text import format_text
from item import ItemContainer


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = ItemContainer(items)

    def __str__(self):
        return (
            format_text(f"You are standing in the {self.name}")
            + "\n"
            + format_text(self.description)
        )

    def move(self, direction):
        try:
            return getattr(self, f"{direction}_to")
        except AttributeError:
            #print (f"Error: No room found for direction '{direction}'")
            return None

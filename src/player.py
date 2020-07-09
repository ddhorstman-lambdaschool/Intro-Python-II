from item import ItemContainer

class Player:
    def __init__(self, name="New Player", location=None, items=[]):
        self.name = name
        self.location = location
        self.items = ItemContainer(items)

    def __str__(self):
        return f"{self.name}, currently located in {self.location}"

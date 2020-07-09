# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name="New Player", location=None, inventory=[]):
        self.name = name
        self.location = location
        self.inventory = inventory

    def __str__(self):
        return f"{self.name}, currently located in {self.location}"

from format_text import format_text


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return (
            self.name
            + "\n"
            + format_text(self.description)
        )

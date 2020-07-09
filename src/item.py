from format_text import format_text


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return format_text(f"{self.name} - {self.description}")

class ItemContainer:
    def __init__(self, items):
        self.items = items

    def __str__(self):
        return "\n".join([i.__str__() for i in self.items])
    
    def __len__(self):
        return len(self.items)

    def add(self, item):
        self.items.append(item)
    
    def remove(self, item_name):
        for idx, item in enumerate(self.items):
            if item.name.lower() == item_name.lower():
                return self.items.pop(idx)
        return None
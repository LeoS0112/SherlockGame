from random import randint


def pre_parse_names(names):
    names = names.replace(" ", "_").replace(",", "").replace("'", "").replace(":", "").replace(";", "").replace("!", "").replace("?", "").replace(".", "").replace("(", "").replace(")", "").replace("-", "").replace(" ", "_")
    return names.lower()


class Room:
    def __init__(self, name, dimensions, description, summary, npcs):
        self.npcs = npcs
        self.description = description
        self.name = pre_parse_names(name)
        self.summary = summary

        # tile_path = get_image_tile(f"carpet2.png", "", f"{name}.png")

class Character:
    def __init__(self, name, description, usefulness, weapon=None, item=None):
        self.name = pre_parse_names(name)
        self.description = description
        self.usefulness = usefulness
        self.weapon = None
        self.items = None
        if weapon is not None:
            self.weapon = pre_parse_names(weapon[0])
            self.weapon_strength = weapon[1]
        if item is not None:
            item_name = pre_parse_names(item)
            self.items = [Item(item_name, randint(1, 10))]      
    
    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        return self.description
    


class Item:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return(f"{self.name} with a score of {self.score}")
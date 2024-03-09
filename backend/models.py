from random import randint
from stability import get_image_tile, stability_use
import os

def pre_parse_names(names):
    names = names.replace(" ", "_").replace(",", "").replace("'", "").replace(":", "").replace(";", "").replace("!", "").replace("?", "").replace(".", "").replace("(", "").replace(")", "").replace("-", "").replace(" ", "_")
    return names.lower()


class Room:
    def __init__(self, name, description, summary, npcs):
        self.npcs = npcs
        self.description = description
        self.name = pre_parse_names(name)
        self.summary = summary

        tile_path = get_image_tile(f"carpet2.png", "", f"images/{self.name}.png")

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

        # If character already in directory, then use the image
        out_path = f"images/{self.name}.png"
        try_path = f"cached_characters/{self.name}.png"

        if os.path.exists(out_path):
            person_path = out_path

        elif os.path.exists(try_path):
            # Copy the file to the images folder
            print(f"Copying {out_path} to {try_path}")
            os.system(f"cp {try_path} {out_path}")
            person_path = out_path

        else:
            print(f"Creating {out_path}")
            person_path = stability_use(out_path, f"Create a character called {self.name} with a description of {self.description}")
                

    

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        return f'{self.name}'
    
    def __repr__(self):
        return f'{self.name}'
    


class Item:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return(f"{self.name} with a score of {self.score}")
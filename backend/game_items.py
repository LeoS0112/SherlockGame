from prolog import sherlock_logic
from gpt_utils import get_description
from stability import get_image_tile


class Room:
    def __init__(self, name, dimensions, description, npcs):
        self.npcs = npcs
        self.description = description
        self.name = name

        tile_path = get_image_tile(f"carpet2.png", "", f"{name}.png")


class Character():
    def init(self, name):
        self.name = name



description = ""
npcs = {}
game_desc = ("In 'Sherlock Holmes: Shadows of Intrigue,' embody the detective in Victorian London. Solve crimes, "
             "explore scenes, and unravel conspiracies using Holmes' deductive prowess. A mysterious letter at 221B "
             "Baker Street initiates a captivating adventure, testing your intellect in a quest for justice")

room_one_description = ("In 'Sherlock Holmes: Shadows of Intrigue,' embody the detective in Victorian London. Solve "
                        "crimes, explore scenes, and unravel conspiracies using Holmes' deductive prowess.")

room_one_summary = ("John Watson said to Sherlock, we have a new case. Jill walked in and said that her husband has "
                    "disappeared. He was last seen in Canary Wharf. Sherlock agrees to investigate and says that "
                    "Moriarty is involved.")

room_one = Room("221B Baker Street", [], room_one_description, room_one_summary)
description = get_description(game_desc, room_one_description, room_one_summary)
print(description)
test = Room("name", None, description, npcs)

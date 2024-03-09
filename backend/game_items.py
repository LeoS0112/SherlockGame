from gpt_utils import get_description, get_npcs, get_first_room_npcs
from stability import get_image_tile
from json import loads
from prolog import Logic
from textwrap import dedent

def pre_parse_names(names):
    names = names.replace(" ", "_").replace(",", "").replace("'", "").replace(":", "").replace(";", "").replace("!", "").replace("?", "").replace(".", "").replace("(", "").replace(")", "").replace("-", "").replace(" ", "_")
    return names.lower()

def load_npcs(npcs, global_characters):
    print(npcs)
    room_chars = []
    new_chars = []

    characters = loads(npcs) 
    
    i = 1
    for i in range(1, 4):
        if f"Name{i}" in characters:
            if characters[f"Name{i}"] not in global_characters:
                person = Character(characters[f"Name{i}"], characters[f"Description{i}"], characters[f"Usefulness{i}"], characters[f"Weapon{i}"])    
                room_chars.append(person)
                global_characters.append(person)
                new_chars.append(person)
            else:
                # Update the description of the character
                for char in global_characters:
                    if char.name == characters[f"Name{i}"]:
                        char.description = characters[f"Description{i}"]
                        room_chars.append(char)
        else:
            break

    return room_chars, global_characters, new_chars

class Room:
    def __init__(self, name, dimensions, description, summary, npcs):
        self.npcs = npcs
        self.description = description
        self.name = pre_parse_names(name)
        self.summary = summary

        tile_path = get_image_tile(f"carpet2.png", "", f"{name}.png")

class Character:
    def __init__(self, name, description, usefulness, weapon=None):
        self.name = pre_parse_names(name)
        self.description = description
        self.usefulness = usefulness
        self.weapon = None
        if weapon is not None:
            self.weapon = pre_parse_names(weapon[0])
            self.weapon_strength = weapon[1]
        

    def __str__(self):
        return self.description

class Item:
    def __init__(self, name, score):
        self.name = name
        self.score = score

def get_first_room(game_desc, goal, global_characters, sherlock_logic):
    
    starting_room_description = ("In 'Sherlock Holmes: Shadows of Intrigue,' embody the detective in Victorian London. Solve "
                    "crimes, explore scenes, and unravel conspiracies using Holmes' deductive prowess.")
    
    room_one_npcs = loads(get_first_room_npcs(game_desc))
    global_characters += [Character(room_one_npcs["Name"], room_one_npcs["Description"], "8")]
    sherlock_logic.add_character(Character(room_one_npcs["Name"], room_one_npcs["Description"], "8"))
    
    room_one_summary = (f"John Watson said to Sherlock, we have a new case. {room_one_npcs['Name']} has the information: {room_one_npcs['Description']}")
    
    room_one = Room("Baker Street 221B", [], starting_room_description, room_one_summary, room_one_npcs)
    sherlock_logic.add_room(room_one)
    return room_one, global_characters

def get_next_room(game_desc, goal, global_characters, sherlock_logic, prev_room):

    next_description = get_description(game_desc, prev_room)

    current_room_chars, global_characters, new_chars = load_npcs(get_npcs(game_desc, next_description, global_characters), global_characters)

    for char in new_chars:
        sherlock_logic.add_character(char)

    next_description = loads(next_description)
    next_room = Room(next_description["Name"], [], next_description["Description"], "", current_room_chars)

    sherlock_logic.add_room(next_room)

    return next_room, global_characters

if __name__ == "__main__":
    sherlock_logic = Logic()
    global_characters = [ Character("Sherlock", "The detective", "10"), Character("Watson", "Sherlock's Assistant", "7"), Character("Moriarty", "The Villain", "0")]
    for char in global_characters:
        sherlock_logic.add_character(char)

    next_description = ""
    game_desc = ("In 'Sherlock Holmes: Shadows of Intrigue,' embody the detective in Victorian London. Solve crimes, "
                "explore scenes, and unravel conspiracies using Holmes' deductive prowess. A mysterious letter at 221B "
                "Baker Street initiates a captivating adventure, testing your intellect in a quest for justice")
    global_goal = "Catch Moriarty"

    room_one, global_characters = get_first_room(game_desc, global_goal, global_characters, sherlock_logic)
    room_two, global_characters = get_next_room(game_desc, global_goal, global_characters, sherlock_logic, room_one)

  
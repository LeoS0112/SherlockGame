from gpt_utils import get_description, get_npcs, get_first_room_npcs, gpt_characters, gpt_response_mood
from stability import get_image_tile
from json import loads
from prolog import Logic
from textwrap import dedent
from models import Room, Character
import os

from communication import Communication




def load_npcs(npcs, global_characters, sherlock_logic):
    room_chars = []
    new_chars = []

    characters = loads(npcs) 
    
    global_character_names = [char.name for char in global_characters]

    i = 1
    for i in range(1, 4):
        if f"Name{i}" in characters:
            if characters[f"Name{i}"] not in global_character_names:
                person = Character(characters[f"Name{i}"], characters[f"Description{i}"], characters[f"Usefulness{i}"], sherlock_logic , characters[f"Weapon{i}"], characters[f"Item{i}"])   
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



def get_first_room(game_desc, goal, global_characters, sherlock_logic):
    
    starting_room_description = ("In 'Sherlock Holmes: Shadows of Intrigue,' embody the detective in Victorian London. Solve "
                    "crimes, explore scenes, and unravel conspiracies using Holmes' deductive prowess.")
    
    room_one_npcs = loads(get_first_room_npcs(game_desc))
    char = Character(room_one_npcs["Name"], room_one_npcs["Description"], "8", sherlock_logic)
    global_characters += [char]
    sherlock_logic.add_character(char)
    
    room_one_summary = (f"John Watson said to Sherlock, we have a new case. {room_one_npcs['Name']} has the information: {room_one_npcs['Description']}")
    
    room_one = Room("Baker Street 221B", starting_room_description, room_one_summary, room_one_npcs)

    sherlock_logic.add_room(room_one)
    return room_one, global_characters

def get_next_room(game_desc, goal, global_characters, sherlock_logic, prev_room):

    next_description = get_description(game_desc, prev_room)

    current_room_chars, global_characters, new_chars = load_npcs(get_npcs(game_desc, next_description, global_characters), global_characters, sherlock_logic)

    for char in new_chars:
        sherlock_logic.add_character(char)
        sherlock_logic.add_item(char.items[0])

    next_description = loads(next_description)
    next_room = Room(next_description["Name"], next_description["Description"], "", current_room_chars)

    sherlock_logic.add_room(next_room)

    return next_room, global_characters

if __name__ == "__main__":

    # Empty the images folder
    os.system("rm backend/media/npcs/*.png")
    os.system("rm backend/media/carpets/*")
    os.system("rm backend/media/*")

    # backend\media\npcs

    sherlock_logic = Logic()
    global_characters = [ Character("Sherlock", "The detective", "10", sherlock_logic), Character("Watson", "Sherlock's Assistant", "7", sherlock_logic), Character("Moriarty", "The Villain", "0", sherlock_logic)]
    for char in global_characters:
        sherlock_logic.add_character(char)

    next_description = ""
    game_desc = ("In 'Sherlock Holmes: Shadows of Intrigue,' embody the detective in Victorian London. Solve crimes, "
                "explore scenes, and unravel conspiracies using Holmes' deductive prowess. A mysterious letter at 221B "
                "Baker Street initiates a captivating adventure, testing your intellect in a quest for justice")
    global_goal = "Catch Moriarty"

    room_one, global_characters = get_first_room(game_desc, global_goal, global_characters, sherlock_logic)

    room_two, global_characters = get_next_room(game_desc, global_goal, global_characters, sherlock_logic, room_one)

    # print character names
    print([char.name for char in global_characters])

    character = global_characters[-1]

    conversation = Communication(character, sherlock_logic)

    print(character.items[0])




    past_conversations = "None"

    conversation.useful_question()

    for _ in range(10):



        response = input()
        character_names_in_response = gpt_characters(response, global_characters)
        politeness_rating = gpt_response_mood(response)
        print(politeness_rating)
        print(response)

        question = conversation.converse(response, past_conversations, character.items[0], character_names_in_response, politeness_rating)


        info = loads(question)
        print("=====================================")
        print(info)


        if past_conversations == "None":
            past_conversations = f"Question: {info['response']}\nAnswer: {response}\n"
        else:
            past_conversations += f"Question: {info['response']}\nAnswer: {response}\n"

        if info["give_item"]:
            conversation.give_item()
            break


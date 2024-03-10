from gpt import generate_response_gpt
from textwrap import dedent
from json import loads

from openai import OpenAI


def get_description(game_desc, last_room, goal="catch Moriarty"):
    prompt = dedent(f"""\
    
    You are designing a game which is {game_desc}
    The previous room the character was in:
        {last_room.description}
    What the character did in that room:
        {last_room.summary}
    The overall aim of the game: 
        {goal}
        
    Output a description of the next room in the format: {{ "Name": Name, "Description": Room Description}}
""")
    new_room_description = generate_response_gpt(prompt)
    return new_room_description


def get_npcs(game_desc, current_room_description, previous_characters, goal="catch Moriarty"):
    print(previous_characters)

    prompt = dedent(f"""\
    
    You are designing a game which is {game_desc}
    The current room the character is in is:
        {current_room_description}
    The overall aim of the game: 
        {goal}
    If relevant, you can include the previous characters with the exact same names, no alternative names. For example if watson exists do not create a dr john watson.
        {previous_characters}
    Or output new characters Sherlock will meet in the next room.
    Each person has a weapon. The weapon has a strength which is a number between 1 and 10. 1 being weak and 10 being strong.
    Usefulness is a number between 1 and 10, 1 being not useful and 10 being very useful.
    They should also have a item which is a clue to the case and Sherlock will need to collect it.
    The format should be: {{ "Name1": Name1, "Description1": Description1, "Weapon1":[PhysicalWeapon1, WeaponStrength1], "Usefulness1":Usefulness1, "Item1":item1 , "Name2": Name2, "Description2": Description2, "Weapon2": [PhysicalWeapon2, WeaponStrength2], "Usefulness2":Usefulness2, "Item2":item2, ...}}
""")
    npcs = generate_response_gpt(prompt)

    return npcs


def get_first_room_npcs(game_desc, goal="catch Moriarty"):
    prompt = dedent(f"""\
    
    You are designing a game which is {game_desc}
    The overall aim of the game: 
        {goal}
        
    Output a character that the Sherlock and Watson will meet in the first room, who will provide them with a new case. Describe the case they provide which is in Canary Wharf
    The format should be: {{ "Name": "Name", "Description": "Description"}}
    
""")

    new_room_description = generate_response_gpt(prompt)
    print(new_room_description)
    return new_room_description


def gpt_response_mood(response):
    prompt = dedent(f"""\
        Rate this paragraph from 1 to 10, where 1 is the most rude and 10 is the most polite: {response}
        Example Output: 6
        """)
    rating = generate_response_gpt(prompt)
    print(rating)
    return int(rating)


def gpt_characters(response, global_characters):
    character_names = [character.name for character in global_characters]
    prompt = dedent(f"""\
        Check which of these characters {character_names} 
        are mentioned in the response: {response}
        Output only a list of character names that are mentioned in the response in the format: [name1, name2, ...].   

        For example, if the response is "Sherlock and Watson are in the room with Moriarty and they are discussing the case", with the characters ["Sherlock", "Watson"],
        the output should be only: ["Sherlock", "Watson"]      
        """)

    character_names = generate_response_gpt(prompt)
    l = character_names.strip().strip("[]").replace("\"", " ").split(", ")
    l = [x.strip("'").strip() for x in l]
    updated_list = [x for x in l if x in character_names]
    return updated_list


if __name__ == "__main__":
    pass
    # Empty the images folder
    # os.system("rm images/*")

    # global_characters = [ Character("Sherlock", "The detective", "10"), Character("Watson", "Sherlock's Assistant", "7"), Character("Moriarty", "The Villain", "0")]
    # character_list = gpt_characters("Sherlock and Watson are in the room with Moriarty and they are discussing the case", global_characters)
    # print(character_list)
    # print(character_list)


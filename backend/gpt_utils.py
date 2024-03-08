from gpt import generate_response_gpt
from textwrap import dedent
from json import loads


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

def get_npcs(game_desc, current_room_description, previous_characters,   goal="catch Moriarty"):

    prompt = dedent(f"""\
    
    You are designing a game which is {game_desc}
    The current room the character is in is:
        {current_room_description}
    The overall aim of the game: 
        {goal}
    If relevant, you can include the previous characters:
        {previous_characters}
    Or output new characters Sherlock will meet in the next room.
    Each person has a weapon this can be None.
    Usefulness is a number between 1 and 10, 1 being not useful and 10 being very useful.
    The format should be: {{ "Name1": Name1, "Description1": Description1, "Weapon1":PhysicalWeapon1, "Usefulness1":Usefulness1 , "Name2": Name2, "Description2": Description2, "Weapon2": PhysicalWeapon2, "Usefulness2":Usefulness2 ...}}
""")
    npcs = generate_response_gpt(prompt)

    return npcs



def get_first_room_npcs(game_desc , goal="catch Moriarty"):

    prompt = dedent(f"""\
    
    You are designing a game which is {game_desc}
    The overall aim of the game: 
        {goal}
        
    Output a character that the Sherlock and Watson will meet in the first room, who will provide them with a new case. Describe the case they provide which is in Canary Wharf
    The format should be: {{ "Name": Name, "Description": Description}}
""")
    new_room_description = generate_response_gpt(prompt)
    return new_room_description




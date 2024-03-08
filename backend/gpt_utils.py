from gpt import generate_response_gpt
from textwrap import dedent


def get_description(game_desc, last_room, goal="catch Moriarty"):
    prompt = dedent(f"""\
    
    You are designing a game which is {game_desc}
    The previous room the character was in:
        {last_room.description}
    What the character did in that room:
        {last_room.summary}
    The overall aim of the game: 
        {goal}
        
    Output a description of the next room in the format: {{ Name: Name, Description: Room Description}}
""")
    new_room_description = generate_response_gpt(prompt)
    return new_room_description


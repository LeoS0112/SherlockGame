from openai import OpenAI
from gpt import generate_response_gpt
from random import choice

from textwrap import dedent

# This is the communication outline which will need to be translated into the frontend into swift

def say_hello(character, name):
    print(f"Hello {name}, my name is {character.name} and I am a {character.description}.")
    
def ask_question(character, question):
    print(f"{character.name} asks: {question}")

def useful_question(character):


    potential_questions = [
        "What's your guess regarding the clue I currently have?",
        "Any thoughts on the nature of the clue in my possession?",
        "Can you speculate about the clue you think I hold?",
        "Curious to hear your thoughts on the clue I might be carrying. Any ideas?",
        "What's your take on the potential clue I'm holding right now?",
        "Any hypotheses on the type of clue I have?",
        "Care to venture a guess about the clue I currently possess?",
        "Interested to know your opinion on the nature of my current clue. Any ideas?",
        "What clue do you suspect I might be holding?",
        "Can you make an educated guess about the clue I have in my possession?"
    ]



    ask_question(character, choice(potential_questions))

def answer_question(character, answer):
    print(f"{character.name} answers: {answer}")

def give_item(character, item):
    print(f"{character.name} gives {item.name} to Sherlock")
    # Make sure to send to backend to update the logic

def defeat(character, character2):
    print(f"{character.name} defeats {character2.name}")
    # Make sure to use backend to get the logic


def converse(character, prompt, previous_conversations):
    
    prompt = dedent(f"""\

You are a character in a game. Your name is {character.name} and you are {character.description}  You are in a room with Sherlock Holmes and Watson. 
You have a clue to the case in the form of an item {character.item}. You can choose either to give the clue to Sherlock or to keep it based on {character.usefulness} with 1 being least useful and 10 being most useful as well as how good the questions Sherlock asked are.

The question asked is: {prompt}
Respond as the character with open dialogue. If they are close to the answer, give them a hint towards the clue. If they get the answer then you can give them the item, otherwise report to try again.
                    
Here are any previous conversations: {previous_conversations}

Return Format: 
    {{
        "response": ResponseInfo,
        "close_to_answer": true/false,
        "give_item": true/false,
        "next_hint": HintInfo

    }}
    """)
    

    response = generate_response_gpt(prompt)
    return response


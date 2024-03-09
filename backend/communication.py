from openai import OpenAI
from gpt import generate_response_gpt
from random import choice, randint
from textwrap import dedent

# This is the communication outline which will need to be translated into the frontend into swift

class Communication:

    def __init__(self, character, sherlock_logic):
        self.character = character
        self.logic = sherlock_logic

    def say_hello(self, name):
        print(f"Hello {name}, my name is {self.character.name} and I am a {self.character.description}.")
        
    def ask_question(self, question):
        print(f"{self.character.name} asks: {question}")

    def useful_question(self):


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



        self.ask_question(choice(potential_questions))

    def answer_question(self, answer):
        print(f"{self.character.name} answers: {answer}")

    def give_item(self):
        item = self.character.items[0]
        self.logic.give_sherlock_item(item)
        if self.logic.completed_game():
            print("well done you've won the game")
         
        # print(f"{character.name} gives {item.name} to Sherlock")
        # Make sure to send to backend to update the logic


    def fight(self):
        if self.logic.sherlock_defeats(self.character):
            self.logic.give_sherlock_item(self.character.items[0])
        else: 
            print("You lost the fight, Game Over")

    def converse(self, prompt, previous_conversations, goal):
        

        if prompt.upper() == "FIGHT":
            print("You have chosen to fight")
            return self.fight()

        prompt = dedent(f"""\

    You are a character in a game. Your name is {self.character.name} and you are {self.character.description}  You are in a room with Sherlock Holmes and Watson. 
    You have a clue to the case in the form of an item {self.character.items[0].name}. You can choose how useful the clue is to Sherlock or to keep it based on {self.character.usefulness+5} with 1 being least useful and 10 being most useful as well as how good the questions Sherlock asked are.
    
    Here are any previous conversations: {previous_conversations[-300:]}


    The question asked is: {prompt}
    Respond as the character with open dialogue. If they are close to the answer: {goal}, give them a hint towards the clue. If they ask for a hint, give them a signficiant hint. 
    If {prompt} is near to the answer: {goal} then you can give them the item and set get_item to true. This should be lenient and not too strict.
                        

    Return Format: 
        {{
            "response": ResponseInfo,
            "close_to_answer": true/false,
            "give_item": true/false,
            "next_hint": HintInfo

        }}
        """)
        

        response = generate_response_gpt(prompt)

        # response = True

        return response


from pyswip import Prolog
from models import Room, Character, Item

# from game_items import Character, Room, Weapon, Item




class Logic:
    def __init__(self):
        self.sherlock_logic = Prolog()

        self.sherlock_logic.assertz("defeats(X, Y) :- strength(X, A), strength(Y,B), X \\= Y, A > B")
        self.sherlock_logic.assertz("strength(X,Z) :- has_weapon(X, A), weapon(A, Z)")

        self.sherlock_logic.assertz("not_member(X, [])")
        self.sherlock_logic.assertz("not_member(X, [H|T]) :- X \\= H, not_member(X, T)")

        self.sherlock_logic.assertz("sherlock_items([H|T]) :- has_item(sherlock, H), not_member(H, T),  sherlock_items(T)")
        self.sherlock_logic.assertz("sherlock_items([])")

        self.sherlock_logic.assertz("sum_items_list([], 0)")
        self.sherlock_logic.assertz("sum_items_list([H|T], X) :- item(H,A), sum_items_list(T, Y), X is Y + A")
        self.sherlock_logic.assertz("sherlock_total(X) :- sherlock_items(L), sum_items_list(L, X)")
        self.sherlock_logic.assertz("completes_game() :- sherlock_total(X), X > 25")

        self.sherlock_logic.assertz("friends(X, Y, 0.5) :- friends(X, A, 1), friends(Y, A, 1)")

        self.sherlock_logic.assertz("character(sherlock)")

    def add_character(self, character):
        name = character.name
        description = character.description
        weapon = character.weapon
        usefulness = character.usefulness
        if weapon is not None:
            self.sherlock_logic.assertz(f"has_weapon({name}, {weapon})")

        self.sherlock_logic.assertz(f"character({name})")
        self.sherlock_logic.assertz(f"use({name}, {usefulness})")

    def add_room(self, room):
        name = room.name
        description = room.description
        summary = room.summary
        npcs = room.npcs

        # If starts with numbers
        if name[0] in "1234567890":
            name = f"room_{name}"
 
        self.sherlock_logic.assertz(f"room({name})")

    def add_weapon(self, weapon):
        name = weapon.name
        strength = weapon.strength
        self.sherlock_logic.assertz(f"weapon({name}, {strength})")

    def add_item(self, item):
        name = item.name
        score = item.score
        self.sherlock_logic.assertz(f"item({name}, {score})")

    def has_item(self, character, item):
        self.sherlock_logic.assertz(f"has_item({character}, {item})")

    def completed_game(self):
        return len(list(self.sherlock_logic.query("completes_game()"))) == 1

    def give_sherlock_item(self, item):
        self.sherlock_logic.assertz(f"has_item(sherlock, {item.name})")

    def sherlock_defeats(self, character):
        return len(list(self.sherlock_logic.query(f"defeats(sherlock, {character.name})"))) == 1

    def add_friends(self, name1, name2):

        self.sherlock_logic.retractall("friends(X, Y, 0.5) :- friends(X, A, 1), friends(Y, A, 1)")
        self.sherlock_logic.assertz(f"friends({name1}, {name2}, 1)")
        self.sherlock_logic.assertz(f"friends({name2}, {name1}, 1)")
        self.sherlock_logic.assertz("friends(X, Y, 0.5) :- friends(X, A, 1), friends(Y, A, 1)")

    def is_friends(self, character1, character2):
        qr = list(self.sherlock_logic.query(f"friends({character1}, {character2}, Z)"))
        if len(qr) == 0:
            return 0
        else:
            return qr[0]['Z']
        
    def get_all_characters(self):
        value =  list(self.sherlock_logic.query("character(X)"))
        return [val['X'] for val in value]
# query_result = list(sherlock_logic.query("defeats(X, Y)"))
# print(query_result)

if __name__ == "__main__":
    sherlock_logic = Logic()
    # sherlock = Character("sherlock", "Sherlock Holmes", 10)
    # watson = Character("watson", "", 10)
    # mycroft = Character("mycroft", "", 6)
    # moriarty = Character("moriarty", "", 0)
    # sherlock_logic.add_character(sherlock)
    # sherlock_logic.add_character(watson)
    # sherlock_logic.add_character(mycroft)

    # sherlock_logic.add_friends(sherlock, watson)
    # sherlock_logic.add_friends(mycroft, watson)
    # print(sherlock_logic.get_all_characters())
    # print(sherlock_logic.is_friends(watson, sherlock))
    # print(sherlock_logic.is_friends(mycroft, sherlock))
    # print(sherlock_logic.is_friends(moriarty, sherlock))



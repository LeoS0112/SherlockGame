from pyswip import Prolog

class Logic:
    def __init__(self):
        self.logic = Prolog()
        self.logic.assertz("defeats(X, Y) :- strength(X, A), strength(Y,B), X \\= Y, A > B")
        self.logic.assertz("strength(X,Z) :- has_weapon(X, A), weapon(A, Z)")

    #define add character
    def add_character(self, character):
        name = character.name
        description = character.description
        weapon = character.weapon
        usefulness = character.usefulness
        if weapon is not None:
            self.logic.assertz(f"has_weapon({name}, {weapon})")

        self.logic.assertz(f"character({name})")
        self.logic.assertz(f"use({name}, {usefulness})")

    def add_room(self, room):
        name = room.name
        description = room.description
        summary = room.summary
        npcs = room.npcs

        self.logic.assertz(f"room({name})")

    def add_weapon(self, weapon):
        name = weapon.name
        self.logic.assertz(f"weapon({name}, strength)")

# query_result = list(sherlock_logic.query("defeats(X, Y)"))
# print(query_result)
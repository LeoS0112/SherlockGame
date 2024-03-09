from pyswip import Prolog


# from game_items import Character, Room, Weapon, Item

class Character:
    def __init__(self, name, description, usefulness, weapon=None):
        self.name = (name)
        self.description = description
        self.usefulness = usefulness
        self.weapon = None
        if weapon is not None:
            self.weapon = (weapon[0])
            self.weapon_strength = weapon[1]

    def __str__(self):
        return self.description


class Item:
    def __init__(self, name, score):
        self.name = name
        self.score = score


class Logic:
    def __init__(self):
        self.logic = Prolog()

        self.logic.assertz("defeats(X, Y) :- strength(X, A), strength(Y,B), X \\= Y, A > B")
        self.logic.assertz("strength(X,Z) :- has_weapon(X, A), weapon(A, Z)")

        self.logic.assertz("not_member(X, [])")
        self.logic.assertz("not_member(X, [H|T]) :- X \\= H, not_member(X, T)")

        self.logic.assertz("sherlock_items([H|T]) :- has_item(sherlock, H), not_member(H, T),  sherlock_items(T)")
        self.logic.assertz("sherlock_items([])")

        self.logic.assertz("sum_items_list([], 0)")
        self.logic.assertz("sum_items_list([H|T], X) :- item(H,A), sum_items_list(T, Y), X is Y + A")
        self.logic.assertz("sherlock_total(X) :- sherlock_items(L), sum_items_list(L, X)")
        self.logic.assertz("completes_game() :- sherlock_total(X), X > 25")

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

    def new_item(self, item):
        name = item.name
        score = item.score
        self.logic.assertz(f"item({name}, {score})")

    def has_item(self, character, item):
        self.logic.assertz(f"has_item({character}, {item})")

    def completed_game(self):
        return len(list(sherlock_logic.logic.query("completes_game()"))) == 1

# query_result = list(sherlock_logic.query("defeats(X, Y)"))
# print(query_result)

if __name__ == "__main__":
    sherlock_logic = Logic()
    sherlock_logic.add_character(Character("sherlock", "Sherlock Holmes", 10))

    # Give Sherlock some items
    sherlock_logic.new_item(Item("pipe", 10))
    # sherlock_logic.new_item(Item("magnifying_glass", 5))
    # sherlock_logic.new_item(Item("notebook", 5))
    # sherlock_logic.new_item(Item("pen", 5))
    # sherlock_logic.new_item(Item("hat", 5))

    sherlock_logic.has_item("sherlock", "pipe")
    # sherlock_logic.has_item("sherlock", "magnifying_glass")
    # sherlock_logic.has_item("sherlock", "notebook")
    # sherlock_logic.has_item("sherlock", "pen")
    # sherlock_logic.has_item("sherlock", "hat")
    qr = list(sherlock_logic.logic.query("has_item(sherlock, X)"))

    query_result = list(sherlock_logic.logic.query("sherlock_total(X)"))
    print(query_result)
    print(sherlock_logic.completed_game())


from prolog import sherlock_logic


class Room:
    def init(self, tile, dimensions):
        pass


class Character():
    def init(self, name):
        self.name = name
        print("hello")
        sherlock_logic.assertz("holds(sherlock, gun)")


a = Character("user")

print(list(sherlock_logic.query("holds(sherlock, gun)")))
print(list(sherlock_logic.query("defeats(sherlock, watson)")))

query_result = list(sherlock_logic.query("defeats(X, Y)"))
print(query_result)
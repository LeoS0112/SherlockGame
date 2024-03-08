from pyswip import Prolog

sherlock_logic = Prolog()
sherlock_logic.assertz("character(sherlock)")
sherlock_logic.assertz("character(watson)")
sherlock_logic.assertz("holds(watson, sword)")
sherlock_logic.assertz("holds(sherlock, gun)")
sherlock_logic.assertz("item(sword)")
sherlock_logic.assertz("item(gun)")
sherlock_logic.assertz("defeats(X, Y) :- holds(X, gun), holds(Y, sword)")


query_result = list(sherlock_logic.query("defeats(X, Y)"))
print(query_result)
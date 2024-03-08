from pyswip import Prolog

prolog = Prolog()
prolog.assertz("character(sherlock)")
prolog.assertz("character(watson)")
prolog.assertz("holds(watson, sword)")
prolog.assertz("holds(sherlock, gun)")
prolog.assertz("item(sword)")
prolog.assertz("item(gun)")
prolog.assertz("defeats(X, Y) :- holds(X, gun), holds(Y, sword)")


query_result = list(prolog.query("defeats(X, Y)"))
print(query_result)


Falsy et truthy
================

Expressions après un if
-----------------------

Jusqu'ici les expressions qu'on a utilisées donnait un booléens une fois évaluées, mais
un expression apès un ``if`` peut être d'un autre type.

Par exemple, un entier::

    x = 0
    if x:
        print("x n'est pas nul")
    else:
        print("x est nul")

    # affiche: x est nul

On dit que ``0`` est ``Falsy``, parce qu'après un ``if``, il se comporte comme une expression
qui vaudrait False.

Réciproquement, tous les entiers sauf 0 sont ``Truthy``, parce qu'ils se comportent comme
une expression qui vaudrait True::

    y = 6
    if y:
        print("y n'est pas nul")
    else:
        print("y est nul")

    # affiche: y n'est pas nul


On retrouve ce principe avec les chaînes de caractères::

    message = ""
    if message:
        print("le message n'est pas vide")
    else:
        print("le message est vide")
    # affiche: le message est vide


Le chaînes vides sont falsy, les autres sont truthy.


Expressions quelconques
-----------------------

En fait, on peut utiliser tous les opérateurs booléens avec des expressions
quelconques::

    message = "bonjour"
    if not message:
        print("le message n'est pas vide")
    # affiche : le message n'est pas vide


    score = 42
    if message and score:
        print("le message et le score sont truthy")
    # affiche : le message et le score sont truthy




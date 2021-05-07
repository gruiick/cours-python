Expressions, instructions, et variables
=======================================

Instructions
------------

Pour l'instant, dans tous les exemples de code, chaque ligne qu'on a écrit
contenait une *instruction*.

Un instruction a un effet sur le programme dans lequel elle est présente.

Par exemple, l'instruction ``print("bonjour")`` affiche "bonjour" dans
le terminal. On dit que l'instruction est *exécutée*.

En règle générale, les instructions sont exécutées une par une, de haut en bas.

Expressions
-----------

Les instructions peuvent contenir des *expressions*.

Un expression est toujours *évaluée* pour retourner une
*valeur*.

Par exemple, ``1 + 2`` est une expression qui renvoie la valeur ``3``
une fois évaluée.

Elle est constituée de 3 éléments :

* le *littéral* 1 ;
* *l'opérateur* ``+`` ;
* le *littéral* 2.

Pour évaluer une expression, Python remplace les littéraux
par leur valeur, puis calcule la valeur finale en
utilisant les opérateurs.

Notez que les expressions peuvent être imbriquées : ::

    1 + (2 * 3)

À droite du plus, on a une expression ``2 + 3``. Quand Python
évaluera l'expression, il verra d'abord le littéral ``1`` et le ``+``,
puis il évaluera l'expression à droite (``2 * 3 = 6``), et finalement
l'expression en entier (``1 + 6 = 7``).

Notez que si vous écrivez une ligne contenant une *expression*,
elle est évaluée mais rien n'est exécuté : ::

    print("Bonjour")
    40 + 2
    print("Au revoir")
    # Affiche: 'Bonjour' puis 'Au revoir'

Ici l'expression ``40 + 2`` a été évaluée, mais Python n'a rien fait
avec le résulat, il est simplement passé à l'instruction suivante.

Variables et valeurs
--------------------

On peut associer des *variables* à des *valeurs* en les plaçant
de part et d'autre du signe ``=`` : on appelle cette opération
une *assignation* : ::

    a = 2

Ici on assigne l'entier 2 à la variable ``a``.

Notez qu'une assignation *n'est pas* une expression, c'est une
*instruction*.

Si plus tard dans le code, on utilise le nom de la variable,
tout se passera comme si le nom de la variable avait été
remplacé par sa valeur : ::

   a = 2
   print(a)
   # affiche: 2

Variables et expressions
------------------------

En fait, on peut assigner n'importe qu'elle *expression* à une variable,
et pas simplement des littéraux : ::

    a = 1 + 2
    print(a)
    # affiche: 3


Variables et expressions contenant d'autres variables
-----------------------------------------------------

Les expressions peuvent également contenir des variables.

Quand Python évalue une expression qui contient des noms de variables,
il remplace celles-ci par leur valeur : ::

    a = 1
    print(a + 2)   # ici "a" a été remplacé par 1
    # affiche: 3

Notez que la valeur de la variable `a` n'a pas changé : ::

    a = 1
    print(a + 2)
    # affiche: 3
    print(a)
    # affiche: 1

Autres exemples : ::

    x = 1
    y = 2
    print(x+y)  # ici x a été remplacé par 1 et y par 2
    # affiche: 3

Changer la valeur d'une variable
--------------------------------

On peut aussi *changer* la valeur d'une variable en assignant
une nouvelle valeur à celle-ci : ::

    a = 2
    print(a)
    a = 3
    print(a)
    # affiche: 2, puis 3

Combiner opération et assignation
---------------------------------

La notation ``+=`` permet de combiner addition et assignation :
les deux exemples ci-dessous sont équivalents : ::

   x = 3
   x = x + 1

::

   x = 3
   x += 1


Cela fonctionne aussi pour ``-=``, ``/=``, etc.

Nom des variables
-----------------

Ci-dessus j'ai utilisé des noms de variables à une lettre,
mais il est préférable d'avoir des noms longs et descriptifs.

Aussi, la convention est de :

* les écrire en minuscules ;
* de séparer les mots par des tirets bas (*underscore*) : ::

   score = 42
   âge_moyen = 22

On dit qu'on utilise le *snake case* (parce que ça ressemble vaguement
à un serpent)

Notez que certains mots ne peuvent pas être utilisés comme nom
de variables. On les appelle des *mots-clés*. La liste
est disponible ici: https://docs.python.org/fr/3/reference/lexical_analysis.html#keywords

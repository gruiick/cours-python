Expressions, instructions, et variables
=======================================

Instructions
------------

Pour l'instant, dans tous les exemples de code, chaque ligne qu'on a écrit
contenait une *instruction*.

Un instruction a un effet sur le programe dans lequel elle est présented

Par exemple, l'expression ``print("bonjour")`` affiche "bonjour" dans
le terminal. On dit que l'expression est *exécutée*.

En règle générale, les expressions sont éxécutées une par une, de haut en bas.

Expressions
-----------

Les instructions peuvent contenir des *expressions*.

Un expression est toujours *évaluée* pour retourner une
*valeur*

Par exemple, ``1 + 2`` es une expression qui renvoie la valeur ``3``
une fois évaluée.

Elle est constituée de 3 éléments:

* Le *littéral* 1
* L'*opérateur* ``+``
* Le *littéral* 2

Pour évaluer une expression, Python remplace les littéraux
par leur valeur, puis calcule la valeur finale en
utilisant les opérateurs.

Notez que les expressions peuvent être imbriquées ::

    1 + (2 * 3)

À droite du plus, on a une expression ``2 + 3``. Quand Python
évaluera l'expression, il verra d'abord le littéral ``1`` et le ``+``,
puis il évaluera l'expression à droite (``2*3 = 6``), et finalement
l'expression en entier (``1 + 6 = 7``).

Variables et valeurs
--------------------

On peut associer des *variables* à des *valeurs* en les plaçant
de part et d'autre du signe ``=`` : on appelle cette opération
une *affectation*::

    a = 2

Ici on assigne l'entier 2 à la variable ``a``.

Notez qu'une affectation *n'est pas* une expression, c'est une
*instruction*.

Si plus tard dans le code, on utilise le nom de la variable,
tout se passera comme si nom de la variable avait été
remplacé par sa valeur::



   a = 2
   print(a)
   # affiche: 2

Variables et expressions
-------------------------

En fait, on peut assigner n'importe qu'elle *expression* à une variable,
et pas simplement des littéraux::

    a = 1 + 2
    print(a)
    # affiche: 3


Variables et expressions contenant d'autres variables
------------------------------------------------------

Les expressions peuvent également contenir des variables.

Quand Python évalue une expression qui contient des noms de variables,
il remplace celles-ci par leur valeur::

    a = 1
    print(a + 2)   # ici a a été remplacé par 1
    # affiche: 3

Notez que la valeur de variable `a` n'a pas changé::

    a = 1
    print(a + 2)
    # affiche: 3
    print(a)
    # affiche: 1

Autres exemples::

    x = 1
    y = 2
    print(x+y)  # ici x a été remplacé par 1 et y par 2
    # affiche: 3

Changer la valeur d'une variable
---------------------------------

On peut aussi *changer* la valeur d'une variable en affectant
une nouvelle valeur à celle-ci::


    a = 2
    print(a)
    a = 3
    print(a)
    # affiche: 2, puis 3

Combiner opération et affectation
----------------------------------

La notation ``+=`` permet de combiner addition et affectation :
les deux exemples ci-dessous sont équivalents::

   x = 3
   x = x + 1

::

   x = 3
   x += 1


Cela fonctionne aussi pour ``-=``, ``/=`` etc.

Nom des variables
-----------------

Ci-dessus j'ai utilisé des noms de variables à une lettre,
mais il est préférable d'avoir des noms longs et descriptifs

Aussi, la convention est de:

* Les écrire en minuscules
* De séparer les mots par des tirets bas (*underscore*)::

   score = 42
   âge_moyen = 22

Notez que certains noms ne peuvent être utilisés comme nom
de variables. On les appelle des *mots-clés*. La liste
est disponible ici: https://docs.python.org/fr/3/reference/lexical_analysis.html#keywords

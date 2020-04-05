Variables
=========

Expressions
-----------

Un peu de vocabulaire avant de continuer.

Quand on écrit ``1 + 2`` en Python, on a ce qu'on
appelle une *expression* -

Un expression est toujours *évaluée* pour retourner une
*valeur* (ici 3)

Quand on écrit ``print(1 + 2)`` on a une *instruction*.

Un instruction ne renvoie pas de valeur, mais a un
effet sur le programme, ici l'affichage de la valeur
de l'expression évaluée dans le terminal.

Enfin, l'expression ``1 + 2`` est constituée de trois
éléments:

* Le *litéral* 1
* L'*opérateur* ``+``
* Le *litéral* 2

Pour évaluer une expression, Python remplace les litéraux
par leur valeur, puis calcule la valeur finale en
utilisant les opérateurs.

Variables et valeurs
--------------------

On peut associer des *variables* à des *valeurs* en les plaçant
de part et d'autre du signe ``=`` : on appelle cette opération
une *assignation*::


    a = 2

Notez qu'une assignation *n'est pas* une expression, c'est une
*instruction*.

On dit aussi que ``a`` est une *référence* vers la valeur ``2``.

Si plus tard dans le code, on utilise le nom de la variable,
tout se passera comme si nom de la variable avait été
remplacé par sa valeur::

   a = 2
   print(a)
   # affiche: 2

Variables et expressions
-------------------------

En fait, on peut assigner une variable à n'importe quelle
*expression*, et pas simplement des littéraux::

    a = 1 + 2
    print(a)
    # affiche: 3


Variables et expressions contenant d'autres variables
------------------------------------------------------

Les expressions peuvent également contenir des variables.

Quand Python évalue une expression qui contient des noms de variables,
il remplace celles-ci par leur valeur::

    x = 1
    y = 2
    z = x + y
    print(z)
    # affiche: 3

Ici on a créé ``z`` en *évaluant* l'expression ``x+y``.

Changer la valeur d'une variable
---------------------------------

On peut aussi *changer* la valeur d'une variable en l'assignant
à une nouvelle valeur::


    a = 2
    print(a)
    a = 3
    print(a)
    # affiche: 2, puis 3

Combiner opération et assignation
----------------------------------

La notation ``+=`` permet de combiner addition et assignation::

   x = 3
   x = x + 1
   print(x)
   # affiche :: 4

   x = 3
   x += 1
   print(x)
   # affiche :: 4


Cela fonctionne aussi pour ``-=``, ``/=`` etc.

Nom des variables
-----------------

Ci-dessus j'ai utilisé des noms de variables à une lettre, comme en maths,
mais il est préférable d'avoir des noms longs et descriptifs

Aussi, la convention est de:

* Les écrire en minuscules
* De séparer les mots par des tirest bas (*underscore*)::

   score = 42
   age_moyen = 22

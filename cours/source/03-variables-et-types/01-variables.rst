Variables
=========

On peut associer des *variables* à des *valeurs* en les plaçant
de part et d'autre du signe `=`: on appelle cette opération
une *assignation*.

Ensuite, on peut utiliser la variable à la place de sa valeur:
à chaque fois que l'interpréteur essaye d'exécuter du code,
il commence par remplacer les variables par leurs valeurs::

    a = 2
    print(a)
    # affiche: 2

    b = 3
    print(a + b)
    # affiche: 5


On peut aussi *changer* la valeur d'une variable en l'assignant
à une nouvelle valeur::


    a = 2
    print(a)
    # affiche: 2

    a = 3
    print(a)
    # affiche: 3


Nom des variables
-----------------

Ci-dessus j'ai utilisé des noms de variables à une lettre, comme en maths,
mais il est préférable d'avoir des noms longs et descriptifs

Aussi, la convention est de:

* Les écrire en minuscules
* De séparer les mots par des tirest bas (*underscore*)::

   score = 42
   age_moyen = 22

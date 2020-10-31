Principes fondamentaux
======================

Définition
----------

Une liste est une *suite ordonnée* d'éléments.

Créer une liste
---------------

Avec des crochets: ``[``, ``]``, et les éléments séparés par des virgules::

    liste_vide = []
    trois_entiers = [1, 2, 3]


Listes hétérogènes
------------------

On peut mettre des types différents dans la même liste::

    ma_liste = [True, 2, "trois"]

On peut aussi mettre des listes dans des listes::

    liste_de_listes = [[1, 2], ["Germaine", "Gertrude"]]

Connaître la taille d'une liste
-------------------------------

Avec ``len()`` - encore une fonction native::

    liste_vide = []
    taille = len(liste_vide)
    print(taille)
    # affiche:  0

    trois_entiers = [1, 2, 3]
    taille = len(trois_entiers)
    print(taille)
    # affiche:  3

Concaténation de listes
-----------------------

Avec ``+``::

    prénoms = ["Alice", "Bob"]
    prénoms += ["Charlie", "Eve"]
    print(prénoms)
    # affiche: ['Alice', 'Bob', "Charlie", 'Eve']

On ne peut concaténer des listes que avec d'autres listes::

    scores = [1, 2, 3]
    scores += 4
    # erreur

    scores += [4]
    print(scores)
    # affiche: [1,2,3,4]

Test d'appartenance
-------------------

Avec ``in``::

    prénoms = ["Alice", "Bob"]
    print("Alice" in prénoms)
    # affiche: True

    prénoms = ["Alice", "Bob"]
    print("Charlie" in prénoms)
    # affiche: False

Modifier une liste
-------------------

Encore une assignation::

    fruits = ["pomme", "orange", "poire"]
    fruits[0] = "abricot"
    print(fruits)
    # affiche: ["abricot", "orange", "poire"]

Indéxer une liste
------------------

* Avec ``[]`` et un entier

* Les index valides vont de 0 à ``n-1`` où ``n`` est la
  taille de la liste::

    fruits = ["pomme", "orange", "poire"]

    print(fruits[0])
    # affiche: "pomme"

    print(fruits[1])
    # affiche: "orange"

    print(list[2])
    # affiche: "poire"

    fruits[3]
    # erreur: IndexError


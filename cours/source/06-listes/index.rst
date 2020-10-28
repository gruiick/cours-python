Chapitre 6 - Listes
===================

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

Itérer sur les éléments d'une liste
------------------------------------

Avec les mots-clés ``for`` et `` in``::

   prénoms = ["Alice", "Bob", "Charlie"]
   for prénom in prénoms:
       # Chaque élément de la liste est assigné tour à tour
       # à la variable 'prénom"
       print("Bonjour", prénom)

.. code-block:: text

   Bonjour Alice
   Bonjour Bob
   Bonjour Charlie

break
-----

Comme pour les boucles `while`, on peut interrompre la boucle `for` avec `break`::

   prénoms = ["Alice", "Bob", "Charlie"]
   for prénom in prénoms:
       if prénom == "Bob":
           break
       print("Bonjour", prénom)

.. code-block:: text

   Bonjour Alice
   Bonjour Charlie

continue
--------

On peut interrompre l'exécution *du bloc courant* (et uniqument le
bloc courant)  avec le mot-clé ``continue``::

   prénoms = ["Alice", "Bob", "Charlie"]
   for prénom in prénoms:
       if prénom == "Bob":
           continue
       print("Bonjour", prénom)

.. code-block:: text

   Bonjour Alice
   Bonjour Charlie


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

Modifier une liste
-------------------

Encore une assignation::

    fruits = ["pomme", "orange", "poire"]
    fruits[0] = "abricot"
    print(fruits)
    # affiche: ["abricot", "orange", "poire"]

Les strings sont aussi des listes (presque)
--------------------------------------------

On peut itérer sur les caractères d'une string::

    for c in "vache":
    	print(c)

.. code-block: console

   v
   a
   c
   h
   e

On peut tester si un caractère est présent::

    print("e" in "vache")
    # affiche: True

    print(x" in "vache")
    # affiche: False


Mais on ne peut pas modifier une string::

   prénom = "Charlotte"
   l = prénom[0]
   print(l)
   # affiche: "C"

   l = prénom[3]
   print(l)
   # affiche: "r"

   prénom[0] = "X"
   # erreur: TypeError


Falsy et truthy
----------------


En réalité on peut mettre autre chose qu'une comparaison ou une variable booléenne après le if.

Si on met une liste vide, ``if`` se comportera comme si on avait mis une valeur fausse, et si
la liste n'est pas vide , ``if`` se comportera comme si on avait mis une valeur vraie.::

    ma_liste = [1, 2, 3]
    if ma_liste:
        print("ma_liste n'est pas vide")
    # affiche: ma_liste n'est pas vide

    mon_autre_liste = []
    if not mon_autre_liste:
        print("mon_autre_liste est vide")
    # affiche: mon_autre_liste est vide

On dit que les listes vides sont *Falsy* et les listes non-vides *Truthy*

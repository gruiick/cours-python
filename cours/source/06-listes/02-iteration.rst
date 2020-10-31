Itération
=========

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


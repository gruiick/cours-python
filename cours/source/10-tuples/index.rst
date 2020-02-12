Chapitre 10 - tuples
=====================
Définition
------------

Un tuple est un ensemble *ordonné* et *immuable* d'éléments. Le nombre, l'ordre et la valeur des éléments sont fixes.

Création de tuples
------------------

Avec des parenthèses::

    tuple_vide = ()
    tuple_à_un_élement = (1,)   # notez la virgule
    tupble_à_deux_éléments = (1, 2)   # on dit aussi: "couple"

Sauf pour le tuple vide, c'est la *virgule* qui fait le tuple

Note: tous les tuples sont truthy, sauf les tuples vides.

Tuples hétérogènes
-------------------

Comme les listes, les tuples peuvent contenir des éléments de types différents::

    # Un entier et une string
    mon_tuple = (42, "bonjour")

    # Un entier et un autre tuple
    mon_tuple = (21, (True, "au revoir"))

Accès
-----

Avec ``[]`` et l'index de l'élément dans le tuple::

    mon_tuple = (42, "bonjour")
    mon_tuple[0]
    42
    mon_tuple[1]
    "bonjour"

Modification
------------

Interdit::

    mon_tuple = (42, "bonjour")
    mon_tuple[0] = 44
    TypeError: 'tuple' object does not support item assignment


Test d'appartenance
-------------------

Avec ``in``:

   >>> mon_tuple = (42, 14)
   >>> 42 in mon_tuple
   True

   >>> 14 in mon_tuple
   True
   >>> 13 in mon_tuple
   False

Déstructuration
----------------

Créer plusieurs variables en une seule ligne::

    >>> couple = ("Batman", "Robin")
    >>> héros, side_kick = couple
    >>> héros
    'Batman'
    >>> side_kick
    'Robin'


Quelques erreurs classiques
---------------------------

.. code-block:: python

   >>> héros, side_kick, ennemi = couple
   ValueError (3 != 2)

   >>> (héros,) = couple
   ValueError (1 != 2)

   # Gare à la virgule:
   >>> héros, = couple
   ValueError (1 != 2)

Pièges
------

.. code-block::

   f(a, b, c)   # appelle f() avec trois arguments

   f((a, b, c)) # appelle f() avec un seul argument
                # (qui est lui-même un tuple à 3 valeurs)

   f(())        # appelle f() avec un tuple vide


   (a)      # juste la valeur de a entre parenthèses
   (a,)     # un tuple à un élément, qui vaut la valeur de a

On peut aussi déstructurer des listes::

    >>> fruits = ["pomme", "banane", "orange"]
    >>> premier, deuxième, troisième = fruits
    >>> premier
    "pomme"
    >>> deuxième
    "banane"
    >>> troisième
    "orange"

On dit aussi: unpacking

Utilisations des tuples
------------------------

Pour simplifier des conditions::

    # Avant:
    if (
       ma_valeur == "nord" or
       ma_valeur == "sud" or
       ma_valeur == "ouest" or
       ma_valeur == "est"):
       		print("direction", ma_valeur)

    # Après:
    if ma_valeur in ("nord", "sud", "est", "ouest"):
       		print("direction", ma_valeur)

Pour retourner plusieurs valeurs::

    def tire_carte():
        valeur = "10"
        couleur = "trèfle"
        return (valeur, couleur)

    v, c = tire_carte()
    print(v, "de", c)
    # 10 de trèfle

Ce n'est pas une nouvelle syntaxe, juste de la manipulation de tuples!

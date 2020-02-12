Chapitre 7 - Listes
===================

// TODO: split in pages

Définition
----------

Une liste est une _suite ordonée_ d'éléments.

Créer une liste
---------------

Avec des crochets: ``[``, ``]``, et les élements séparés par des virgules::

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

    >>> liste_vide = []
    >>> len(liste_vide)
    0
    >>> trois_entiers = [1, 2, 3]
    >>> len(trois_entiers)
    3

Concaténation de listes
-----------------------

Avec ``+``::

    >>> prénoms = ["Alice", "Bob"]
    >>> prénoms += ["Charlie", "Eve"]
    >>> prénoms
    ['Alice', 'Bob', "Charlie", 'Eve']

On ne peut concaténer des listes que avec d'autres listes::

    >>> scores = [1, 2, 3]
    >>> scores += 4  # TypeError
    >>> scores += [4]  # OK

Test d'appartenance
-------------------

Avec ``in``::

    >>> prénoms = ["Alice", "Bob"]
    >>> "Alice" in prénoms
    True

    >>> prénoms = ["Alice", "Bob"]
    >>> "Charlie" in prénoms
    False

Itérer sur les élements d'une liste
------------------------------------

Avec ``for ... in``::

   prénoms = ["Alice", "Bob", "Charlie"]
   for prénom in prénoms:
   	# La variable 'prénom" est assignée à chaque
   	# élément de la liste
       print("Bonjour", prénom)

   Bonjour Alice
   Bonjour Bob
   Bonjour Charlie

## Indéxer une liste

* Avec `[]` et un entier

* Les index valides vont de 0 à `n-1` où `n` est la
taille de la liste.

```python
>>> fruits = ["pomme", "orange", "poire"]
>>> fruits[0]
"pomme"
>>> fruits[1]
"orange"
>>> list[2]
"poire"
>>> fruits[3] # IndexError
```

## Modifier une liste

Encore une assignation:

```python
>>> fruits = ["pomme", "orange", "poire"]
>>> fruits[0] = "abricot"
>>> fruits
["abricot", "orange", "poire"]
```

## Les strings sont aussi des listes (presque)

On peut itérer sur les caractères d'une string:

```python
for c in "vache":
	print(c)
v
a
c
h
e
```

On peut tester si un caractère est présent:

```python
>>> "e" in "vache"
True
>>> "x" in "vache"
False
```


Mais on neut peut pas modifier une string

```python
>>> prénom = "Charlotte"
>>> prénom[0]
"C"
>>> prénom[3]
"r"
>>> prénom[0] = "X" # TypeError
```


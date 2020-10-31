Listes et booléens
==================

Falsy et truthy
----------------

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

Test d'appartenance
-------------------

On peut tester si un élément est dans une liste avec le mot-clé ``in``::

    prénoms = ["Alice", "Bob"]
    print("Alice" in prénoms)
    # affiche: True

    prénoms = ["Alice", "Bob"]
    print("Charlie" in prénoms)
    # affiche: False


Comparaisons de listes
-----------------------

On peut utiliser l'opérateur ``==`` avec deux listes de part et
d'autres. Les listes seront considérées comme égales si

* Elles ont la même taille
* Tous leurs éléments sont égaux un à un en respectant l'ordre::

    [1] == [2]        # False
    [1, 2] == [2, 1]  # False
    [1, 2] == [1, 2]  # True


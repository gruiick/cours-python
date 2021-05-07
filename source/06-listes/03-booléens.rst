Listes et booléens
==================

Falsy et truthy
---------------

Si on met une liste vide, ``if`` se comportera comme si on avait mis une valeur fausse, et si
la liste n'est pas vide , ``if`` se comportera comme si on avait mis une valeur vraie : ::

    ma_liste = [1, 2, 3]
    if ma_liste:
        print("ma_liste est truthy")
    else:
        print("ma_liste est falsy")
    # affiche: ma_liste est truthy

    mon_autre_liste = []
    if mon_autre_liste:
        print("mon_autre_liste n'est pas vide")
    else:
        print("mon_autre_liste est vide")
    # affiche: mon_autre_liste est vide

On dit que les listes vides sont *Falsy* et les listes non-vides *Truthy*.

Test d'appartenance
-------------------

On peut tester si un élément est dans une liste avec le mot-clé ``in`` : ::

    prénoms = ["Alice", "Bob"]
    print("Alice" in prénoms)
    # affiche: True

    prénoms = ["Alice", "Bob"]
    print("Charlie" in prénoms)
    # affiche: False


Comparaisons de listes
----------------------

On peut utiliser l'opérateur ``==`` avec deux listes de part et
d'autre. Les listes seront considérées comme égales si :

* elles ont la même taille ;
* tous leurs éléments sont égaux un à un en respectant l'ordre : ::

    x = [1]
    y = [1, 2]
    print(x == y)
    # affiche: False, x et y n'ont pas la même taille

    x = [1, 2]
    y = [1, 3]
    print(x == y)
    # affiche: False, x et y n'ont pas les mêmes éléments

    x = [1, 2]
    y = [2, 1]
    print(x == y)
    # affiche: False, x et y ont les mêmes éléments, mais
    # pas dans le bon ordre

    x = [1, 2]
    y = [1]
    y += [2]
    print(x == y)
    # affiche: True, x et y ont les mêmes éléments, dans le même ordre

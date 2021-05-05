Relation avec les strings
=========================

Les strings sont aussi des listes (presque).

On peut itérer sur les *caractères* d'une string::

    for c in "vache":
        print(c)

.. code-block:: console

   v
   a
   c
   h
   e

On peut tester si un caractère est présent::

    print("e" in "vache")
    # affiche: True

    print("x" in "vache")
    # affiche: False


Notez qu'on peut aussi utiliser ``in`` pour tester si
une chaîne de caractères est contenue dans une autre::

    print("ch" in "vache")
    # affiche: True

On peut indexer une string::

   prénom = "Charlotte"
   l = prénom[0]
   print(l)
   # affiche: "C"

Mais on ne peut pas modifier une string en utilisant
l'indexation::

   prénom = "Charlotte"
   prénom[0] = "X"
   # erreur: TypeError

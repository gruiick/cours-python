Relation avec les strings
=========================

Les strings sont aussi des listes (presque).

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

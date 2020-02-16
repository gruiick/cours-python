Chapitre 4 - Booléens et conditions
===================================

En Python, les variables ``True`` et ``False`` sont toujours définies
et servent à représenter une valeur vraie ou fausse.

(Notez qu'elles commencent par une majuscule)

Assignation
-----------

On peut assigner des variables à True ou False::


    la_terre_est_plate = False
    python_c_est_genial = True


Comparaisons
------------

Certaines opérations renvoient des booléens:

+------+-----------------------------+
|``=`` | égal                        |
+------+-----------------------------+
|``!=``| différent                   |
+------+-----------------------------+
|``>`` | strictement supérieur       |
+------+-----------------------------+
|``>=``| supérieur ou égal           |
+------+-----------------------------+
|``<`` | strictement inférieur       |
+------+-----------------------------+
|``<=``| inférieur                   |
+------+-----------------------------+

Par example::

   a = 2
   b = 3
   print(a > b)
   # affiche: False

   print(2 + 2 == 4)
   # affiche: True

.. warning::

    Ne pas confondre: ``==`` pour la comparaison et ``=`` pour l'assignation


Enfin, on peut écrire des encadrements::

    a = 3
    print(2 <= a < 4)
    # affiche: True


not
---

Enfin, on peut utiliser ``not`` pour inverser une condition::

    a = 3
    if not a == 4:
        print("a est différent de 4")
    # affiche: a est différent de 4

    la_terre_est_plate = False
    print(not la_terre_est_plate)
    # affiche: True

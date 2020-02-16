Booléens et conditions
======================

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

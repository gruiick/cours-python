Booléens
========

On appelle *booléenne* une valeur qui peut être soit vraie, soit fausse.

En Python, les littéraux ``True`` et ``False`` représentent respectivement les valeurs
vraies et fausses.

(Notez qu'ils commencent par une majuscule)


Comparaisons
------------

Certaines expressions renvoient des booléens, c'est à dire
soit la valeur ``True``, soit la valeur ``False``

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

Par exemple::

   a = 2
   b = 3
   print(a > b)
   # affiche: False

   print(2 + 2 == 4)
   # affiche: True

.. warning::

    Ne pas confondre: ``==`` pour la comparaison et ``=`` pour l'assignation

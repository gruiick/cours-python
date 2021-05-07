Maths simples
=============

Opérations avec des entiers
---------------------------

On peut utiliser ``+, *, -`` avec des entiers :

.. code-block:: python

   print(1 + 2)
   # affiche: 3

   print(6 - 3)
   # affiche: 3

   print(2 * 4)   # une étoile pour la multiplication
   # affiche: 8

   print(3 ** 2)  # deux étoiles pour l'opération 'puissance'
   # affiche: 9


Opérations avec des flottants
-----------------------------

C'est le ``.`` qui fait le flottant.


.. code-block:: python

   print(0.5 + 0.2)
   # affiche: 0.7

On utilise `/` pour les divisions flottantes : ::

   print(10 / 2)
   # affiche: 5.0 (et non '5')

Notez que les flottants sont imprécis, ce qui explique le `5` à la fin
de l'affichage de la division de 10 par 3 : ::

   print(10 / 3)
   # affiche:3.3333333333333335


Division entières et modulo
---------------------------

14 divisé par 3 font 4 avec un reste de 2.

On peut récupérer le quotient avec `//` et
le reste avec ``%``.

.. code-block:: python

   print(14 // 3)
   # affiche: 4

   print(14 % 3)
   # affiche: 2

.. warning::

   Le ``%`` n'a rien à voir avec un pourcentage !


Priorité des opérations
-----------------------


Comme en maths, la multiplication est prioritaire
sur les autres opérations : ::

    print(1 + 2 * 3)
    # affiche: 7

et on peut utiliser des parenthèses pour grouper les opérations : ::

    print((1 + 2) * 3)
    # affiche: 9


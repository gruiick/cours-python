Exercice
========

Le but de l'exercice est d'afficher un sapin de largeur arbitraire dans
la console, comme ceci:

.. code-block:: text


     #
    ###
   #####
  #######
 #########
     #
     #


Le sapin est composé d'une suite de lignes, chacune des lignes étant
constituée uniquement de dièses.

Il y a deux parties au sapin: les feuilles qui forment un triangle
de largeur 1 tout en haut jusqu'à une ligne de largeur 10 tout en bas,
et un pied constitué de deux dièses superposés


Indices
-------

Pour construire une chaîne de caractères constituée uniquement de
dièses vous pouvez utiliser l'expression suivante:

.. code-block:: python

    cinq_diéses = "#" * 5
    print(cinq_diéses)

.. code-block:: text

    #####



Consignes
---------

Partir du code suivant:

.. literalinclude:: /extraits/sapin.py


* Compléter le code pour afficher le sapin en entier

* Remplacer tous les litéraux (5, 6, 4, 7...) par des expressions utilisant
  la variable  `largeur`

* Demander à l'utilisateur la largeur du sapin en début de programme au lieu
  d'utiliser la valeur litérale `10`.


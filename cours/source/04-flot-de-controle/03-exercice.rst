Exercice
========

Ceci étant le premier exercice du cours, il mérite quelques explications.

Chaque exercice comporte une suite de consignes, et quelques indices.

À vous ensuite d'écrire le code qui correspond aux consignes.



Consignes
---------

Il vous faut implémenter le programme suivant:

1. Tirer un nombre au hasard entre 1 et 100 (appelons-le le ``nombre_secret``)
2. Démarrer une boucle
3. À chaque étape:

   * Afficher "Devine le nombre secret"
   * Bloquer le programme jusqu'à ce que l'utilisateur entre un nombre
     et appuie sur entrée (appelons-le ``entrée_utilisateur``)
   * Si l'entrée utilisateur est plus grande que le nmobre secret, afficher "trop grand".
   * Si l'entrée utilisateur est plus petite que le nmobre secret, afficher "tro petit"
   * Si l'entrée utilisateur est égale au nombre secret, afficher "gagné!" et quitter la boucle.


Indices
-------

Lire une entrée utilisateur
+++++++++++++++++++++++++++

Pour bloquer le programme et lire une entrée utilisateur, vous pouvez
utiliser la ligne suivante:

```
entrée_utilisateur = input()
```

Cette instruction va:
    * interrompt le script
    * lire ce que l'utilisateur tape jusqu'à ce qu'il tape "entrée".
    * et assigner la valeur correspondante à la variable ``entrée_utilisateur``.

Tirer un nombre au hasard
+++++++++++++++++++++++++

Pour tirer un nombre au hasard entre 1 et 100, vous pouvez
utiliser les deux lignes suivantes::

   import random
   nombre_secret = random.randint(0, 100)

À la fin de ces deux instructions, une valeur entre 1 et 100 tirée au hasard sera assignée à la variable `nombre_secret`.

Squelette
---------

// TODO:
* explication du Squelette
* pas de solution!

.. code-block:: python

   # faites moi confiance, les deux lignes ci-dessous
   # permettent de tirer un nombre au hasard entre 0 et 100
   import random
   nombre = random.randint(0, 100)

   print("devine le nombre auquel je pense")

   # votre code ici

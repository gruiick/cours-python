Code source
===========

Définition
-----------------------

Aussi appelé: "code source", ou "source".

L'essence du logiciel libre :)


Notre premier fichier source
-----------------------------


Insérez le code suivant dans votre éditeur de texte

.. code-block:: python

     print("Bonjour, monde")
     # affiche: Bnojour, monde



Oui, juste ces deux lignes.

Sauvegardez dans un fichier `bonjour.py` dans `Documents/e2l/python` par exemple


Lancer du code en ligne de commande
-----------------------------------

Lancez une invite de commandes et tapez quelque chose comme:


.. code-block:: console

   cd Documents/e2l/python/
   python3 bonjour.py

(Utilisez `python` sous Windows)

Si tout se passe bien, vous devrez voir s'afficher ceci:

.. code-block:: text


   Bonjour, monde

Vous savez maintenant comment exécuter du code Python dans n'importe quel fichier:

1. Écrire le code dans un fichier
2. Se rendre dans le répertoire contenant le fichier et lancer `python3`  (ou `python`) suivi du nom du fichier.

print()
-------

Revenons sur ce qu'il s'est passé : nous avions le mot `print` avec des parenthèses
et quelque chose à l'intérieur des parenthèses, et ceci a provoqué l'affichage
du contenu des parenthèses dans le terminal.


Commentaires
------------

La deuxième ligne, quant à elle, a été complètement ignorée par l'interpréteur parce
qu'elle commençait par un ``#``. Il s'agit d'un *commentaire*, et il sert principalement
aux humains qui lisent le code.

Note à propos des examples
---------------------------

La plupart des examples de ce cours contiendront un ou plusieurs appels à
`print` afin d'afficher les opérations que l'interpréteur a effectué.

Pour lire ce cours de manière efficace, il est conseillé de lancer les
examples de code sur votre machine, et de vérifier si ce qui est
affiché sur votre machine correspond à ce qui est écrit dans le cours.

Il est aussi recommandé de **ne pas** copier/coller le code.

À la place, prenez le temps de retaper le code dans votre éditeur.

Plusieurs raisons à cela:

* Recopier le code vous aidera à vous souvenir de la syntaxe
* Si vous faites des erreurs, Python vous préviendra et vous
  découvrirer les erreurs courantes
* Il est possible que des erreurs subsistent dans ce cours,
  et procéder ainsi nous permettra de les corriger.

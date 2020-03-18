Jouons avec les fonctions
=========================

Introduction
------------

Reprenons ce qu'on a vu jusqu'ici.

D'une part, on peut créer des variables en les assignant à une valeur::

    # Création d'une variable `x` avec la valeur 4
    x = 4


D'autre part, on peut définir et appeler des fonctions::

    # Définition de la fonction:
    def dire_bonjour(nom):
        print("Bonjour " + nome

    # Appel
    dire_bonjour("Max")

    # Affiche: "Bonjour Max"


Fonctions en tant que variables
-------------------------------

Il se trouve qu'en Python, on peut assigner des variables à ... des fonctions

.. code-block:: python

  # Définition d'une fonction `dire_bonjour_en_français`
  def dire_bonjour_en_français(nom):
      print("Bonjour " + nom)

  # Définition d'une fonction `dire_bonjour_en_anglais`
  def dire_bonjour_en_anglais(nom):
      print("Hello " + nom)

  # Création d'une variable qui pointe sur la fonction française:
  ma_fonction_qui_dit_bonjour = dire_bonjour_en_français

  # Appel de la fonction:
  ma_fonction_qui_dit_bonjour("Max")

  # Affiche: Bonjour Max


De façon cruciale, notez que l'on n'a *pas* mis de parenthèses à droite
lorsqu'on a créé la variable `ma_fonction_qui_dit_bonjour`.

On peut donc dire que lorsqu'on définit une fonction avec `def()` et un corps
il y a en réalité deux étapes:

1. Python stocke le corps de la fonction quelque part
2. Il crée une variable pointant vers ce corps

En Python, il est assez fréquent d'utiliser de code tel que celui-ci, souvent avec un dictionnaire:

Fonctions en tant qu'argement d'autres fonctions
------------------------------------------------

On a vu en début de chapitre qu'on peut créé des variables qui pointent
vers des fonctions.

Du coup, rien n'empêche de les passer en *argument* d'autres fonctions.

Par exemple::

    def appelle_deux_fois(f):
        f()
        f()


    def crier():
        print("Aline !")

    appelle_deux_fois(crier)

    # Affiche:
    # Aline !
    # Aline !


Fonctions imbriquées
--------------------

On peut aussi définir une fonction dans une autre fonction::

    TODO


Fonctions retournant des fonctions
----------------------------------

Enfin, on peut retourner une fonction depuis une autre fonction::

    def fabrique_fonction_qui_additionne(n):
        def fonction_résultat(x):
            return x + n
        return fonction_résultat


    additionne_2 = fabrique_fonction_qui_additionne(2)
    y = additionne_2(5)
    print(y)
    # Affiche: 7


Un autre paradigme
-------------------

Le fait qu'on puisse traiter les fonctions comme n'importe quelle
autre valeur (c'est-à-dire les assigner à des variables, les passer
en argument et les retourner)

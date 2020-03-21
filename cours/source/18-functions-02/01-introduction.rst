Jouons avec les fonctions
=========================

Introduction
------------

Reprenons ce qu'on a vu jusqu'ici.

D'une part, on peut créer des variables en les assignant à une valeur::

    # Création d'une variable `x` avec la valeur 4
    x = 4


On dit aussi que ``x`` *référence* la valeur ``4``

D'autre part, on peut définir et appeler des fonctions::

    # Définition de la fonction:
    def dire_bonjour(nom):
        print("Bonjour " + nom)

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

  # Création d'une variable qui référence la fonction française:
  ma_fonction_qui_dit_bonjour = dire_bonjour_en_français

  # Appel de la fonction:
  ma_fonction_qui_dit_bonjour("Max")

  # Affiche: Bonjour Max


De façon cruciale, notez que l'on n'a *pas* mis de parenthèses à droite
lorsqu'on a créé la variable `ma_fonction_qui_dit_bonjour`.

On peut donc dire que lorsqu'on définit une fonction avec `def()` et un corps
il y a en réalité deux étapes:

1. Python stocke le corps de la fonction quelque part
2. Il crée une variable qui référence ce corps

En Python, il est assez fréquent d'utiliser de code tel que celui-ci, souvent avec un dictionnaire::

    fonctions_connues = {
       "français": dire_bonjour_en_français,
       "anglais": dire_bonjour_en_anglais,
    }

    # Ici on stocke la langue parlée par l'utilisateur
    # et son prénom
    langue_parlée = ...
    prénom = ....

    if langue_parlée in fonctions_connues:
        fonction = fonctions_connues[langue_parlée]
        fonction(prénom)


Fonctions en tant qu'argement d'autres fonctions
------------------------------------------------

On a vu en début de chapitre qu'on peut créé des variables qui référencent
des fonctions.

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


    def affiche_message(message):
        def affiche():
            print(message)

    affiche_message("Bonjour")
    # affiche: Bonjour

Deux notes importantes:

Premièrement, la fonction `affiche()` qui est imbriquées dans `affiche_message()` n'est pas
accessible à l'éxtérieur de la fonction qui la contient. En d'autres termes, ce code
ne fonctionne pas::

    def affiche_message(message):
        def affiche():
            print(message)

    affiche()
    # NameError: 'affiche' is not defined

C'est un mécanisme similaire aux :ref:`portées des variables <portées-des-variables>` vu précédemment.

Deuxièment, la fonction `affiche()` à l'intérieur de `affiche_message()`
a accès à l'argument `message` de la fonction `affiche_message`. On appelle
ça une "closure".



Fonctions retournant des fonctions
----------------------------------

En réalité, on combine souvent les closures avec des fonctions qui
retournent d'autres fonctions::


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
en argument et les retourner), est caractéristique des langages
dits "fonctionnels". Python est donc **à la fois** un
langages *impératif*, *objet* et *fonctionnel*. On dit que
c'est un langage *multi-paradigme*.


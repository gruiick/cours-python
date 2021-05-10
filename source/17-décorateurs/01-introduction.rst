Jouons avec les fonctions
=========================

Introduction
------------

Reprenons ce qu'on a vu jusqu'ici.

D'une part, on peut créer des variables en assignant des valeurs à celles-ci : ::

    # Création d'une variable `x` avec la valeur 4
    x = 4

D'autre part, on peut définir et appeler des fonctions : ::

    # Définition de la fonction:
    def dire_bonjour(nom):
        print("Bonjour " + nom)

    # Appel
    dire_bonjour("Max")

    # Affiche: "Bonjour Max"


Fonctions en tant que variables
-------------------------------

Il se trouve qu'en Python, on peut assigner des fonctions à des
variables. C'est différent d'assigner le résultat de l'appel à une
fonction à une variable, et ça permet de retarder l'appel :

.. code-block:: python

  # Définition d'une fonction `dire_bonjour_en_français`
  def dire_bonjour_en_français(nom):
      print("Bonjour " + nom)

  # Définition d'une fonction `dire_bonjour_en_anglais`
  def dire_bonjour_en_anglais(nom):
      print("Hello " + nom)

  # Assigne une fonction à la variable - aucune fonction
  # n'est appelée à ce stade.
  ma_fonction_qui_dit_bonjour = dire_bonjour_en_français

  # Appel de la fonction (retardé)
  ma_fonction_qui_dit_bonjour("Max")

  # Affiche: Bonjour Max


De façon cruciale, notez que l'on n'a *pas* mis de parenthèses à droite
lorsqu'on a créé la variable ``ma_fonction_qui_dit_bonjour``.

On peut donc dire que lorsqu'on définit une fonction avec ``def ma_fonction()`` 
et un corps, il y a en réalité deux étapes :

1. Python stocke le corps de la fonction quelque part ;
2. Il assigne le corps de celle-ci à une variable dont le nom est ``ma_fonction``.

En Python, il est assez fréquent d'utiliser un code tel que celui-ci, souvent 
avec un dictionnaire : ::

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


Fonctions en tant qu'argument d'autres fonctions
------------------------------------------------

On a vu en début de chapitre qu'on peut assigner des fonctions à des variables.

Du coup, rien n'empêche de passer des fonctions en *argument* d'autres fonctions.

Par exemple : ::

    def appelle_deux_fois(f):
        f()
        f()

    def crier():
        print("Aline !")

    appelle_deux_fois(crier)

    # affiche:
    # Aline !
    # Aline !


Fonctions imbriquées
--------------------

On peut aussi définir une fonction dans une autre fonction : ::


    def affiche_message(message):
        def affiche():
            print(message)
        affiche()

    affiche_message("Bonjour")
    # affiche: Bonjour

Deux notes importantes :

Premièrement, la fonction ``affiche()`` qui est imbriquées dans ``affiche_message()`` 
n'est pas accessible à l'extérieur de la fonction qui la contient. En d'autres 
termes, ce code ne fonctionne pas : ::

    def affiche_message(message):
        def affiche():
            print(message)

    affiche()
    # NameError: 'affiche' is not defined

C'est un mécanisme similaire aux :ref:`portées des variables <portées-des-variables>` 
vu précédemment.

Deuxièment, la fonction ``affiche()`` à l'intérieur de ``affiche_message()``
a accès à l'argument ``message`` de la fonction ``affiche_message()``. On appelle
ça une "closure".


Fonctions retournant des fonctions
----------------------------------

En réalité, on combine souvent les closures avec des fonctions qui
retournent d'autres fonctions : ::


    def fabrique_fonction_qui_additionne(n):
        def fonction_résultat(x):
            return x + n
        return fonction_résultat


    additionne_2 = fabrique_fonction_qui_additionne(2)
    y = additionne_2(5)
    print(y)
    # affiche: 7


Un autre paradigme
------------------

Le fait qu'on puisse traiter les fonctions comme n'importe quelle
autre valeur (c'est-à-dire les assigner à des variables, les passer
en argument et les retourner), est caractéristique des langages
dits "fonctionnels". Python est donc **à la fois** un
langage *impératif*, *objet* et *fonctionnel*. On dit que
c'est un langage *multi-paradigmes*.


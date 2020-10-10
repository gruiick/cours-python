Fonctions
=========

Fonctions sans argument
-----------------------

Définition::

    def dire_bonjour():
        print("Bonjour")


* avec le mot-clé `def`
* avec un `:` à la fin et un *bloc indenté* (appelé *le corps de la fonction*).

Appel::

    dire_bonjour()

* avec le nom de la fonction et des parenthèses

Exemple complet::

    def dire_bonjour():
        print("Bonjour")

    dire_bonjour()
    # Affiche: bonjour'

* Le *nom* de la fonction est le mot utilisé pour la définir et l'appeler
* Le *corps* de la fonction est le bloc après le `def()`

* Quand on *définit* une fonction, on associe un nom avec un corps.
* Quand on *appelle* une fonction, on exécute le corps.

Le pouvoir des fonctions
------------------------

Ici on vient de créer une nouvelle fonctionnalité
à Python. Avant qu'on définisse la fonction
`dire_bonjour()`, il ne savait pas dire bonjour,
il savait uniquement afficher des messages à
l'écran.

On dit qu'on a *créé une abstraction*. Et
c'est une technique extrêmement utile en
programmation.


Fonction avec un argument
--------------------------

Définition: avec l'argument à l'intérieur des parenthèses::

    def dire_bonjour(prénom):
        print("Bonjour " + prénom)

Appel: en passant une variable ou une valeur dans les parenthèses::

    dire_bonjour("Germaine")

Pour évaluer une expression qui contient l'appel a une fonction, on:

* assigne le contenu des parenthèses aux arguments de la fonction
* puis on éxécute les instructions dans le corps de la fonction

.. code-block::

    # Ceci:
    dire_bonjour("Dimitri")

    # Est équivalent à cela:
    prénom_de_dimitri = "Dimitri"
    print("Bonjour " + prénom_de_dimitri)

    # Lui-même équivalent à:
    print("Bonjour " + "Dimitri")

Exemple complet::


    def dire_bonjour(prénom):
        print("Bonjour " + prénom)
    dire_bonjour("Germaine")
    # affiche: Bonjour Germaine

    prénom_de_charlotte = "Charlotte"
    dire_bonjour(prénom_de_charlotte)
    # affiche: Bonjour Charlotte


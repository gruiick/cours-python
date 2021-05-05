Chapitre 11 - Introduction aux modules
======================================

Un fichier = un module
------------------------

Et oui, vous faites des modules sans le savoir depuis le début :)

Un fichier `foo.py` correspond *toujours* module `foo`

**Attention: Ce n'est pas tout à fait réciproque. Le module `foo` peut venir d'autre chose
qu'un fichier foo.py.**

Importer un module
------------------

Ou: accéder à du code provenant d'un *autre* fichier source.

Créons un fichier `bonjour.py` contenant seulement une assignation
de l'entier 42 à la variable `a`::

    # Dans bonjour.py
    a = 42

Comme un fichier = un module, on vient de crée un module ``bonjour`` contenant une variable ``a``.

Si maintenant on crée un fichier ``salutations.py`` dans le même répertoire,
on peut accéder à cette variable en *important* le module avec le mot-clé
``import``::

    # Dans salutations.py
    import bonjour
    print(bonjour.a)
    # affiche: 42


.. note::

  Le nom du module est écrit directement, ce n'est *pas* une
  chaîne de caractères.

On voit que la variable `a` dans `bonjour.py` est devenue
un *attribut* du module `bonjour` lorsque `bonjour` a été importé


Si maintenant on rajoute une fonction ``dire_bonjour`` dans ``bonjour.py``::

    # Dans bonjour.py
    a = 42
    def dire_bonjour():
        print("Bonjour!")

On peut appeler la fonction ``dire_bonjour`` depuis ``salutations.py``
en utilisant l'attribut ``dire_bonjour`` du module ``bonjour``::

   # Dans salutations.py
   import bonjour
   bonjour.dire_bonjour()
   # affiche: Bonjour!

Les imports ne sont faits qu'une seule fois
-------------------------------------------

Il est important de noter que:

* **tout** le code à l'intérieur d'un module est éxécuté lors du premier import
* mais il n'est *pas* ré-éxécuté si le module a déjà été importé auparavant.

On peut le voir en mettant du code dans `bonjour.py`,
en plus des simples définitions de fonctions et de créations
de variables::

    # Dans bonjour.py
    print("Je suis le module bonjour et tu viens de m’importer")
    def dire_bonjour():
        ....

.. code-block:: python

    # Dans salutation.py
    import bonjour
    # affiche: Je suis le module bonjour et tu viens de m’importer

    import bonjour
    # n'affiche rien


La bibliothèque standard
------------------------

La bibliothèque standard est une collection de modules directement utilisables fournis à l'installation de Python.

Exemple: ``sys``, ``random``, ...

Toute la bibliothèque standard est documentée - et la traduction en Français est en cours:

https://docs.python.org/fr/3/library/index.html

Mettez ce lien dans vos favoris - il vous sera très utile.

Quelques examples de modules de la bibliothèque standard
---------------------------------------------------------

Easter eggs
++++++++++++

(Ou fonctionnalités cachées)

* ``import antigravity``
* ``import this``

Je vous laisse découvrir ce que fait le premier. Quant au deuxième, il contient
une liste de préceptes que la plupart des développeurs Python s'efforcent de
respecter. On en reparlera ...


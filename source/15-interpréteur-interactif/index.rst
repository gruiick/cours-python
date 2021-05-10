Chapitre 15 - L'interpréteur interactif
=======================================

Démarrage
---------

Jusqu'ici, on a toujours lancé la commande Python avec ``python`` suivi du nom
d'un fichier source.

Il est égalemnet possible de lancer la commande ``python3`` sans argument.

Dans ce cas, on se retrouve avec une **autre** invite de commandes :

.. code-block:: console

    $ python3
    Python 3.7.1 (default, Oct 22 2018, 10:41:28)
    [GCC 8.2.1 20180831] on linux
    Type "help", "credits" or "license" for more information.
    >>>

Deux invites de commandes
-------------------------

Notez les trois chevrons: ``>>>``. Cela vous permet de différencier l'invite
de commandes du système d'exploitation de celle de Python.

* Système d'exploitation -> Python : taper ``python3`` (sans arguments).
* Python -> Système d'exploitation : taper ``quit()``.

Fonctionnement de l'interpréteur
--------------------------------

L'interpréteur fonctionne dans une boucle :

1. Lire le code qui a été tapé (soit une ligne, soit une succession de blocs) ;
2. Évaluation du code qui a été entré ;
3. Affichage de la valeur le cas échéant ;
4. Retour au début.

(En anglais, on dit "REPL" pour "read/eval/print/loop")

Example d'une session interactive : ::

    >>> a = 42
    >>> a
    42
    >>> b = 4
    >>> a + b
    46


Notez que si la variable est None, l'interpréteur n'affiche rien : ::

    >>> def ne_fait_rien():
            pass
    >>> résultat = ne_fait_rien()
    >>> résultat
    >>> résultat is None
    True



Interpréteur interactif et imports
----------------------------------

Recréons un fichier ``bonjour.py`` contenant : ::

    # dans bonjour.py
    salutation = "Bonjour,"
    def dire_bonjour(nom):
        print(salutation, nom)


On peut démarrer un interpréteur interactif dans le répertoire
contenant le fichier ``bonjour`.py``, et "jouer" avec
les attributs du module bonjour : ::

    >>> import bonjour
    >>> bonjour.dire_bonjour("Bob")
    Bonjour, Bob

    >>> bonjour.salutation = "Hello,"
    >>> bonjour.dire_bonjour("Bob")
    Hello, Bob


.. warning::

    Si le contenu de bonjour.py change, il faut *relancer*
    l'interpréteur interactif et refaire l'import.

Exceptions natives
==================

Les exceptions sont toujours des instances de classes, et les classes d'exceptions 
héritent toujours  de la classe ``BaseException``.

Le nom de l'exception est en réalité le nom de la classe, ici l'exception levée 
par la ligne ``return 1 / 0`` est une instance de la classe ``ZeroDivisionError``.

Cette exception fait partie des nombreuses exceptions prédéfinies en Python. 
Ensemble, elles forment une *hiérarchie d'exceptions* dont voici un extrait :

.. code-block:: text


    BaseException
    +-- SystemExit
    +-- KeyboardInterrupt
    +-- Exception
        +-- ArithmeticError
        |   +-- ZeroDivisionError
        +-- LookupError
        |   +-- IndexError
        |   +-- KeyError
        +-- OSError
        |   +-- FileNotFoundError
        +-- TypeError
        +-- ValueError


IndexError et KeyError
----------------------

``IndexError`` est levée quand on essaye d'accéder à un index trop grand
dans une liste : ::

    ma_liste = ["pomme"]
    ma_liste[2] = "abricot"

    # IndexError: list assignment index out of range

``KeyError`` est levée quand on essaye d'accéder à une clé qui n'existe pas
dans un dictionnaire : ::

    scores = { "Alice" : 10 }
    score_de_bob = scores["Bob"]

    # KeyError: 'Bob'

Notez que la description de ``KeyError`` est la valeur de la clé manquante.

ValueError
----------

``ValueError`` est levée (entre autres) quand on tente une mauvaise conversion : ::

   entrée_utilisateur = "pas un nombre"
   valeur = int(entrée_utilisateur)


KeyboardInterrupt
-----------------

``KeyboardInterrupt`` est levée quand on fait ``ctrl-c``.


FileNotFoundError
-----------------

``FileNotFoundError`` est levée quand on essaye d'ouvrir, en lecture, un 
fichier qui n'existe pas : ::


    with open("fichier-inexistant.txt", "r") as f:
        contenu = f.read()


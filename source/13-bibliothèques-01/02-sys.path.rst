sys.path
========

En Python, il existe une variable ``path`` prédéfinie dans le module ``sys`` qui fonctionne de manière similaire
à la variable d'environnement ``PATH``.

Si j'essaye de l'afficher sur ma machine, voici ce que j'obtiens::

    import sys
    print(sys.path)

.. code-block:: text

    [
     "",
     "/usr/lib/python3.8",
     "/usr/lib/python3.8/lib-dynload",
     "/home/dmerej/.local/lib/python3.8/",
     "/usr/lib/python3.8/site-packages",
    ]

Le résultat dépend:
 * du système d'exploitation
 * de la façon dont Python a été installé
 * et de la présence ou non de certains réportoires.

En fait, ``sys.path`` est construit dynamiquement par l'interpréteur Python au démarrage.

Notez également que ``sys.path`` commence par une chaîne vide. En pratique, cela signifie que le répertoire courant a la priorité sur tout le reste.

Priorité du répertoire courant
------------------------------

Prenons un exemple. Si vous ouvrez un explorateur de fichiers dans le deuxième
élément de la liste de ``sys.path`` (``/usr/lib/python3.8/`` sur ma machine), vous trouverez
un grand nombre de fichiers Python.

notamment, vous devriez trouver un fichier ``random.py`` dans ce répertoire.

En fait, vous trouverez la plupart des modules de la bibliothèque standard dans
ce répertoire.

Maintenant, imaginons que vous avez un deuxième fichier ``random.py`` dans votre répertoire courant. Finalement, imaginez
que vous lancez un fichier ``foo.py`` contentant ``import random`` dans ce même réportoire.

Et bien, c'est le fichier ``random.py`` de votre répertoire qui sera utilisé, et non celui de la bibliothèque standard!

Permissions des répertoires de sys.path
---------------------------------------

Un autre aspect notable de ``sys.path`` est qu'il ne contient que deux
répertoires dans lesquels l'utilisateur courant peut potentiellement écrire
: le chemin courant et le chemin dans ``~/.local/lib``. Tous les autres
(``/usr/lib/python3.8/``, etc.) sont des chemins "système" et ne peuvent
être modifiés que par un compte administrateur (avec ``root`` ou ``sudo``, donc).

La situation est semblable sur macOS et Windows.

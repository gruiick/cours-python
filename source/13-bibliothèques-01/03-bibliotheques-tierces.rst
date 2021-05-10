Bibliothèques tierces
=====================

Prenons un exemple : ::

    # dans foo.py
    import tabulate

    scores = [
      ["John", 345],
      ["Mary-Jane", 2],
      ["Bob", 543],
    ]
    table = tabulate.tabulate(scores)
    print(table)

.. code-block:: console

   $ python3 foo.py
   ---------  ---
   John       345
   Mary-Jane    2
   Bob        543
   ---------  ---

Ici, le module ``tabulate`` n'est ni dans la bibliothèque standard, ni écrit 
par l'auteur du script ``foo.py``. On dit que c'est une bibliothèque tierce.

On peut trouver `le code source de tabulate
<https://bitbucket.org/astanin/python-tabulate/src/master/>`_ facilement.
La question qui se pose alors est : Comment faire en sorte que ``sys.path`` 
contienne le module ``tabulate`` ?

Eh bien, plusieurs solutions s'offrent à vous.

Le gestionnaire de paquets
--------------------------

Si vous utilisez une distribution Linux, peut-être pourrez-vous utiliser votre 
gestionnaire de paquets :

.. code-block:: console

   $ sudo apt install python3-tabulate

Comme vous lancez votre gestionnaire de paquets avec ``sudo``, celui-ci sera 
capable d'écrire dans les chemins système de ``sys.path``.

À la main
---------

Une autre méthode consiste à partir des sources : Par exemple, si le paquet de 
votre distribution n'est pas assez récent, ou si vous avez besoin de modifier le 
code de la bibliothèque en question.

Voici une marche à suivre possible :

1. Récupérer les sources de la version qui vous intéresse dans la `section 
   téléchargement de bitbucket <https://bitbucket.org/astanin/python-tabulate/downloads/?tab=tags>`_ ;
2. Extraire l'archive, par exemple dans ``src/tabulate`` ;
3. Se rendre dans ``src/tabulate`` et lancer ``python3 setup.py install --user``.

Anatomie du fichier setup.py
----------------------------

La plupart des bibliothèques Python contiennent un ``setup.py`` à la racine de 
leurs sources. Il sert à plein de choses, la commande ``install`` n'étant 
qu'une parmi d'autres.


Le fichier ``setup.py`` contient en général simplement un ``import`` de
``setuptools``, et un appel à la fonction ``setup()``, avec de nombreux
arguments : ::

    # tabulate/setup.py
    from setuptools import setup

    setup(
      name='tabulate',
      version='0.8.1',
      description='Pretty-print tabular data',
      py_modules=["tabulate"],
      scripts=["bin/tabulate"],
      ...
    )


Résultat de l'invocation de setup.py
------------------------------------

Par défaut, ``setup.py`` essaiera d'écrire dans un des chemins système de
``sys.path``, d'où l'utilisation de l'option ``--user``.

Voici à quoi ressemble la sortie de la commande :

.. code-block:: console

   $ cd src/tabulate
   $ python3 setup.py install --user
   running install
   ...
   Copying tabulate-0.8.4-py3.7.egg to /home/dmerej/.local/lib/python3.7/site-packages
   ...
   Installing tabulate script to /home/dmerej/.local/bin

Notez que le module a été copié dans ``~/.local/lib/python3.7/site-packages/`` 
et le script dans ``~/.local/bin``. Cela signifie que *tous* les scripts Python 
lancés par l'utilisateur courant auront accès au module ``tabulate``.

Notez également qu'un script a été installé dans ``~/.local/bin``. Une 
bibliothèque Python peut contenir aussi bien des modules que des scripts.

Un point important est que vous n'avez en général pas besoin de lancer le 
script directement. Vous pouvez utiliser ``python3 -m tabulate``. Procéder 
de cette façon est intéressant puisque vous n'avez pas à vous soucier de 
rajouter le chemin d'installation des scripts dans la variable d'environnement 
``PATH``.



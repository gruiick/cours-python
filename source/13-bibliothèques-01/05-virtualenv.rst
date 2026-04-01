Environnements virtuels
=======================

La solution est d'utiliser un environnement virtuel (*virtualenv* en
abrégé). C'est un répertoire *isolé* du reste du système.



Aparté : python3 -m venv sur Debian
-----------------------------------

La commande `python3 -m venv` fonctionne en général partout, dès
l'installation de Python3 (*out of the box*, en Anglais), *sauf* sur Debian
et ses dérivées.

Si vous utilisez Debian, la commande pourrait ne pas fonctionner. En fonction
des messages d'erreur que vous obtenez, il est possible de résoudre le
problème en :

* installant le paquet ``python3-venv`` ;
* ou en utilisant d'abord ``pip`` pour installer ``virtualenv``, avec
  ``python3 -m pip install virtualenv --user`` puis en lançant ``python3 -m
  virtualenv foo-venv``.

Comportement de python dans le virtualenv
-----------------------------------------

Ce répertoire contient de nombreux fichiers et dossiers, et notamment un
binaire dans ``foo-venv/bin/python3``.

Voyons comment il se comporte en le comparant au binaire ``/usr/bin/python3``
habituel :

.. code-block:: console

   $ /usr/bin/python3 -c 'import sys; print(sys.path)'
   ['',
     ...
    '/usr/lib/python3.7',
    '/usr/lib/python3.7.zip',
    '/usr/lib/python3.7/lib-dynload',
    '/home/dmerej/.local/lib/python3.7/site-packages',
    '/usr/lib/python3.7/site-packages'
   ]

.. code-block:: console

   $ /home/dmerej/foo-venv/bin/python -c 'import sys; print(sys.path)'
   ['',
    '/usr/lib/python3.7',
    '/usr/lib/python3.7.zip',
    '/usr/lib/python3.7/lib-dynload',
    '/home/dmerej/foo-venv/lib/python3.7/site-packages,
   ]

À noter :

* Le répertoire "global" dans ``~/.local/lib`` a disparu.
* Seuls quelques répertoires systèmes sont présents (ils correspondent
  plus ou moins à l'emplacement des modules de la bibliothèque standard).
* Un répertoire *au sein* du virtualenv a été ajouté.

Ainsi, l'isolation du virtualenv est reflété dans la différence de la
valeur de ``sys.path``.

Il faut aussi préciser que le virtualenv n'est pas complètement isolé
du reste du système. En particulier, il dépend encore du binaire Python
utilisé pour le créer.

Par exemple, si vous utilisez ``/usr/local/bin/python3.7 -m venv foo-37``,
le virtualenv dans ``foo-37`` utilisera Python 3.7 et fonctionnera tant que
le binaire ``/usr/local/bin/python3.7`` existe.

Cela signifie également qu'il est possible qu'en mettant à jour le paquet
``python3`` sur votre distribution, vous rendiez inutilisables les virtualenvs
créés avec l'ancienne version du paquet.


Comportement de pip dans le virtualenv
--------------------------------------

D'après ce qui précède, le virtualenv ne devrait contenir aucun module
en dehors de la bibliothèque standard et de ``pip`` lui-même.

On peut s'en assurer en lançant ``python3 -m pip freeze`` depuis le virtualenv
et en vérifiant que rien ne s'affiche :

.. code-block:: console

   $ python3 -m pip freeze
   # de nombreuses bibliothèques en dehors du virtualenv
   apipkg==1.5
   cli-ui==0.9.1
   gaupol==1.5
   tabulate==0.8.4

.. code-block:: console

   $ /home/dmerej/foo-venv/bin/python3 -m pip freeze
   # rien :)

On peut alors utiliser le module ``pip`` *du virtualenv* pour installer des
bibliothèques dans celui-ci :

.. code-block:: console

   $ /home/dmerej/foo-venv/bin/python3 -m pip install cli-ui
   Collecting cli-ui
     Using cached https://pythonhosted.org/..cli_ui-0.9.1-py3-none-any.whl
   Collecting colorama (from cli-ui)
     Using cached https://pythonhosted.org/..colorama-0.4.1-py2.py3-none-any.whl
   Collecting unidecode (from cli-ui)
     Using cached https://pythonhosted.org/..Unidecode-1.0.23-py2.py3-none-any.whl
   Collecting tabulate (from cli-ui)
   Installing collected packages: colorama, unidecode, tabulate, cli-ui
   Successfully installed cli-ui-0.9.1 colorama-0.4.1 tabulate-0.8.3
     unidecode-1.0.23

Cette fois, aucune bibliothèque n'est marquée comme déjà installée,
et on récupère donc ``cli-ui`` et toutes ses dépendances.

On a enfin notre solution pour résoudre notre conflit de dépendances :
On peut simplement créer un virtualenv par projet. Ceci nous permettra
d'avoir effectivement deux versions différentes de ``cli-ui``, isolées les
unes des autres.

Activer un virtualenv
---------------------

Devoir préciser le chemin du virtualenv en entier pour chaque commande peut
devenir fastidieux ; heureusement, il est possible *d'activer* un virtualenv,
en lançant une des commandes suivantes :

* ``source foo-venv/bin/activate``, si vous utilisez un shell POSIX ;
* ``source foo-venv/bin/activate.fish``, si vous utilisez Fish ;
* ``foo-venv\bin\activate.bat``, sous Windows.

Une fois le virtualenv activé, taper ``python``, ``python3`` ou ``pip`` utilisera
les binaires correspondants dans le virtualenv automatiquement,
et ce, tant que la session du shell sera ouverte.

Le script d'activation ne fait en réalité pas grand-chose à part modifier
la variable ``PATH`` et rajouter le nom du virtualenv au début de l'invite
de commandes :

.. code-block:: console

   # Avant
   user@host:~/src $ source foo-env/bin/activate
   # Après
   (foo-env) user@host:~/src $

Pour sortir du virtualenv, entrez la commande ``deactivate``.

Les environnements virtuels en pratique
---------------------------------------


Le système de gestions des dépendances de Python peut paraître compliqué
et bizarre, surtout venant d'autres langages.

Mon conseil est de toujours suivre ces deux règles :

* un virtualenv par projet ;
* toujours utiliser ``pip`` *depuis* un virtualenv.

Certes, cela peut paraître fastidieux, mais c'est une méthode qui vous
évitera probablement de vous arracher les cheveux (croyez-en mon expérience).

Voici un exemple d'arborescence qui montre deux projets,
``projet-1`` et ``projet-2``, chacun avec son virtualenv
dédié :

.. code-block:: text

   projets
   ├── projet-1
   │   ├── projet_1.py
   │   └── .venv
   │       ├── bin
   │       ├── include
   │       ├── lib
   │       └── ...
   └── projet-2
       ├── projet_2.py
       └── .venv
           ├── bin
           ├── include
           ├── lib
           └── ...

Notez bien que les sources de chaque projet ``projet_1.py`` et ``projet_2.py``
sont au même niveau que le répertoire ``.venv`` et non à l'intérieur
de celui-ci.

Vous pouvez aussi retenir la règle suivante : étant donné  un répertoire
"X" contenant les sources d'un projet, les commandes à lancer pour créer
le virtualenv seront :

.. code-block:: console

    $ cd X/
    $ python3 -m venv .venv

Pour conclure
-------------

Pour installer `pandas` dans le projet `foo`, trois étapes

1. Créer un virtualenv dans `foo/.venv`
2. Activer le virtualenv 
3. Installer `pandas` en lançant `pip install pandas` depuis le virtualenv

Notez qu'il est possible de faire cela en passant par l'IDE
(VS Code ou PyCharm)

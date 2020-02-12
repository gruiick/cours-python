Bibliothèques tierces
=====================

Prenons un exemple::

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

Ici, le module ``tabulate`` n'est ni dans la bibliothèque standard, ni écrit par l'auteur du script ``foo.py``. On dit que c'est une bibliothèque tierce.

On peut trouver `le code source de tabulate
<https://bitbucket.org/astanin/python-tabulate/src/master/>`_ facilement. La
question qui se pose alors est: comment faire en sorte que `sys.path`
contienne le module ``tabulate``?

Eh bien, plusieurs solutions s'offrent à vous.

Le gestionnaire de paquets
---------------------------

Si vous utilisez une distribution Linux, peut-être pourrez-vous utiliser votre gestionnaire de paquets:

.. code-block:: console

   $ sudo apt install python3-tabulate

Comme vous lancez votre gestionnaire de paquets avec ``sudo``, celui-ci sera capable d'écrire dans les chemins système de ``sys.path``.

À la main
----------

Une autre méthode consiste à partir des sources - par exemple, si le paquet de votre distribution n'est pas assez récent, ou si vous avez besoin de modifier le code de la bibliothèque en question.

Voici une marche à suivre possible :

1. Récupérer les sources de la version qui vous intéresse dans la `section téléchargement de bitbucket <https://bitbucket.org/astanin/python-tabulate/downloads/?tab=tags>`_.
1. Extraire l'archive, par exemple dans ``src/tabulate``
1. Se rendre dans ``src/tabulate`` et lancer ``python3 setup.py install --user``

Anatomie du fichier setup.py
-----------------------------

La plupart des bibliothèques Python contiennent un ``setup.py`` à
la racine de leurs sources. Il sert à plein de choses, la commande ``install``
n'étant qu'une parmi d'autres.


Le fichier ``setup.py`` contient en général simplement un ``import`` de
``setuptools``, et un appel à la fonction ``setup()``, avec de nombreux
arguments::

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
-------------------------------------

Par défaut, ``setup.py`` essaiera d'écrire dans un des chemins système de
``sys.path``, d'où l'utilisation de l'option ``--user``.

Voici à quoi ressemble la sortie de la commande:

.. code-block:: console

   $ cd src/tabulate
   $ python3 setup.py install --user
   running install
   ...
   Copying tabulate-0.8.4-py3.7.egg to /home/dmerej/.local/lib/python3.7/site-packages
   ...
   Installing tabulate script to /home/dmerej/.local/bin

Notez que module a été copié dans ``~/.local/lib/python3.7/site-packages/``
et le script dans ``~/.local/bin``. Cela signifie que *tous* les scripts Python
lancés par l'utilisateur courant auront accès au module ``tabulate``.

Notez également qu'un script a été installé dans ``~/.local/bin`` - Une
bibliothèque Python peut contenir aussi bien des modules que des scripts.

Un point important est que vous n'avez en général pas besoin de lancer le
script directement. Vous pouvez utiliser ``python3 -m tabulate``. Procéder
de cette façon est intéressant puisque vous n'avez pas à vous soucier de
rajouter le chemin d'installation des scripts dans la variable d'environnement
PATH.


Dépendances
-----------

Prenons une autre bibliothèque : ``cli-ui``.

Elle permet d'afficher du texte en couleur dans un terminal::

   import cli_ui

   cli_ui.info("Ceci est en", cli_ui.red, "rouge")

Elle permet également d'afficher des tableaux en couleur::

    headers=["name", "score"]
    data = [
      [(bold, "John"), (green, 10.0)],
      [(bold, "Jane"), (green, 5.0)],
    ]
    cli_ui.info_table(data, headers=headers)

Pour ce faire, elle repose sur la bibliothèque ``tabulate`` vue
précédemment. On dit que ``cli-ui`` *dépend* de ``tabulate``.

Déclaration des dépendances
----------------------------

La déclaration de la dépendance de ``cli-ui`` vers ``tabulate`` s'effectue également dans le fichier ``setup.py``::

    setup(
      name="cli-ui",
      version="0.9.1",
      install_requires=[
         "tabulate",
         ...
      ],
      ...
    )

pypi.org
---------

On comprend dès lors qu'il doit nécessairement exister un *annuaire* permettant de relier les noms de dépendances à leur code source.

Cet annuaire, c'est le site `pypi.org <https://pypi.org/>`_. Vous y trouverez
les pages correspondant à `tabulate <https://pypi.org/project/tabulate/>`_
et `cli-ui <https://pypi.org/project/python-cli-ui/>`_.

pip
---

``pip`` est un outil qui vient par défaut avec Python3[^4]. Vous pouvez également l'installer grâce au script `get-pip.py <https://bootstrap.pypa.io/get-pip.py>`_, en lançant ``python3 get-pip.py --user``.

Il est conseillé de *toujours* lancer ``pip`` avec ``python3 -m pip``. De cette
façon, vous êtes certains d'utiliser le module ``pip`` correspondant à votre
binaire ``python3``, et vous ne dépendez pas de ce qu'il y a dans votre ``PATH``.

``pip`` est capable d'interroger le site ``pypi.org`` pour retrouver les
dépendances, et également de lancer les différents scripts ``setup.py``.

Comme de nombreux outils, il s'utilise à l'aide de *commandes*. Voici
comment installer ``cli-ui`` à l'aide de la commande 'install' de  ``pip``:

.. code-block:: console

   $ python3 -m pip install cli-ui --user
   Collecting cli-ui
   ...
   Requirement already satisfied: unidecode in /usr/lib/python3.7/site-packages (from cli-ui) (1.0.23)
   Requirement already satisfied: colorama in /usr/lib/python3.7/site-packages (from cli-ui) (0.4.1)
   Requirement already satisfied: tabulate in /mnt/data/dmerej/src/python-tabulate (from cli-ui) (0.8.4)
   Installing collected packages: cli-ui
   Successfully installed cli-ui-0.9.1

On constate ici quelques limitations de ``pip``:

* Il faut penser à utiliser ``--user`` (de la même façon que lorsqu'on lance ``setup.py`` à la main)
* Si le paquet est déjà installé dans le système, pip ne saura pas le
mettre à jour - il faudra passer par le gestionnaire de paquet de
  la distribution

En revanche, `pip` contient de nombreuses fonctionnalités intéressantes:

* Il est capable de désinstaller des bibliothèques (à condition toutefois
  qu'elles ne soient pas dans un répertoire système)
* Il est aussi capable d'afficher la liste complète des bibliothèques
  Python accessibles par l'utilisateur courant avec `freeze`.

Voici un extrait de la commande ``python3 -m pip freeze`` au moment de la rédaction de cet article sur ma machine:

.. code-block:: console

   $ python3 -m pip freeze
   apipkg==1.5
   cli-ui==0.9.1
   gaupol==1.5
   tabulate==0.8.4

On y retrouve les bibliothèques ``cli-ui`` et ``tabulate``, bien sûr, mais
aussi la bibliothèque ``gaupol``, qui correspond au [programme d'édition de
sous-titres](https://otsaloma.io/gaupol/) que j'ai installé à l'aide du
gestionnaire de paquets de ma distribution. Précisons que les modules de
la bibliothèque standard et ceux utilisés directement par pip sont omis
de la liste.

On constate également que chaque bibliothèque possède un *numéro de version*.

Numéros de version
-------------------

Les numéros de version remplissent plusieurs rôles, mais l'un des principaux
est de spécifier des changements incompatibles.

Par exemple, pour ``cli-ui``, la façon d'appeler la fonction ``ask_choice``
a changé entre les versions 0.7 et 0.8, comme le montre cet extrait du
`changelog <https://tankerhq.github.io/python-cli-ui/changelog.html#v0-8-0)>`_:

  *The list of choices used by ask_choice is now a named keyword argument:*

   .. code-block::

      # Old (<= 0.7)
      ask_choice("select a fruit", ["apple", "banana"])
      # New (>= 0.8)
      ask_choice("select a fruit", choices=["apple", "banana"])

Ceci s'appelle un *changement d'API*.

Réagir aux changements d'API
-----------------------------

Plusieurs possibilités:

* On peut bien sûr adapter le code pour utiliser la nouvelle API, mais cela
  n'est pas toujours possible ni souhaitable.
* Une autre solution est de spécifier des *contraintes* sur le numéro de
  version dans la déclaration des dépendances. Par exemple::

   setup(
     install_requires=[
       "cli-ui < 0.8",
       ...
     ]
   )

Aparté : pourquoi éviter sudo pip
---------------------------------

Souvenez-vous que les fichiers systèmes sont contrôlés par votre gestionnaire de paquets.

Les mainteneurs de votre distribution font en sorte qu'ils fonctionnent bien les uns
avec les autres. Par exemple, le paquet ``python3-cli-ui`` ne sera mis à jour
que lorsque tous les paquets qui en dépendent seront prêts à utiliser la
nouvelle API.

En revanche, si vous lancez ``sudo pip`` (où ``pip`` avec un compte root),
vous allez écrire dans ces mêmes répertoire et vous risquez de "casser"
certains programmes de votre système.

Mais il y a un autre problème encore pire.

Conflit de dépendances
----------------------

Supposons deux projets A et B dans votre répertoire personnel. Ils dépendent
tous les deux de ``cli-ui``, mais l'un des deux utilise ``cli-ui 0.7`` et l'autre
``cli-ui 0.9``.  Que faire ?


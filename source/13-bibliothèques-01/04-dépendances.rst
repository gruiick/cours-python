Dépendances
===========

Prenons une autre bibliothèque : ``cli-ui``.

Elle permet d'afficher du texte en couleur dans un terminal : ::

   import cli_ui

   cli_ui.info("Ceci est en", cli_ui.red, "rouge")

Elle permet également d'afficher des tableaux en couleur : ::

    headers=["name", "score"]
    data = [
      [(bold, "John"), (green, 10.0)],
      [(bold, "Jane"), (green, 5.0)],
    ]
    cli_ui.info_table(data, headers=headers)

Pour ce faire, elle repose sur la bibliothèque ``tabulate`` vue
précédemment. On dit que ``cli-ui`` *dépend* de ``tabulate``.

Déclaration des dépendances
---------------------------

La déclaration de la dépendance de ``cli-ui`` vers ``tabulate`` s'effectue 
également dans le fichier ``setup.py`` : ::

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
--------

On comprend dès lors qu'il doit nécessairement exister un *annuaire* permettant 
de relier les noms de dépendances à leur code source.

Cet annuaire, c'est le site `pypi.org <https://pypi.org/>`_. Vous y trouverez
les pages correspondant à `tabulate <https://pypi.org/project/tabulate/>`_
et `cli-ui <https://pypi.org/project/python-cli-ui/>`_.

pip
---

``pip`` est un outil qui vient par défaut avec Python3[^4]. Vous pouvez 
également l'installer grâce au script `get-pip.py <https://bootstrap.pypa.io/get-pip.py>`_, 
en lançant ``python3 get-pip.py --user``.

Il est conseillé de **toujours** lancer ``pip`` avec ``python3 -m pip``. De cette
façon, vous êtes certains d'utiliser le module ``pip`` correspondant à votre
binaire ``python3``, et vous ne dépendez pas de ce qu'il y a dans votre ``PATH``.

``pip`` est capable d'interroger le site ``pypi.org`` pour retrouver les
dépendances, et également de lancer les différents scripts ``setup.py``.

Comme de nombreux outils, il s'utilise à l'aide de *commandes*. Voici
comment installer ``cli-ui`` à l'aide de la commande 'install' de  ``pip`` :

.. code-block:: console

   $ python3 -m pip install cli-ui --user
   Collecting cli-ui
   ...
   Requirement already satisfied: unidecode in /usr/lib/python3.7/site-packages (from cli-ui) (1.0.23)
   Requirement already satisfied: colorama in /usr/lib/python3.7/site-packages (from cli-ui) (0.4.1)
   Requirement already satisfied: tabulate in /mnt/data/dmerej/src/python-tabulate (from cli-ui) (0.8.4)
   Installing collected packages: cli-ui
   Successfully installed cli-ui-0.9.1

On constate ici quelques limitations de ``pip`` :

* Il faut penser à utiliser ``--user`` (de la même façon que lorsqu'on lance 
  ``setup.py`` à la main).
* Si le paquet est déjà installé dans le système, pip ne saura pas le
  mettre à jour, il faudra passer par le gestionnaire de paquet de
  la distribution.

En revanche, ``pip`` contient de nombreuses fonctionnalités intéressantes :

* Il est capable de désinstaller des bibliothèques (à condition toutefois
  qu'elles ne soient pas dans un répertoire système).
* Il est aussi capable d'afficher la liste complète des bibliothèques
  Python accessibles par l'utilisateur courant avec ``freeze``.

Voici un extrait de la commande ``python3 -m pip freeze`` au moment de la 
rédaction de cet article sur ma machine :

.. code-block:: console

   $ python3 -m pip freeze
   apipkg==1.5
   cli-ui==0.9.1
   gaupol==1.5
   tabulate==0.8.4

On y retrouve les bibliothèques ``cli-ui`` et ``tabulate``, bien sûr, mais
aussi la bibliothèque ``gaupol``, qui correspond au `programme d'édition de
sous-titres <https://otsaloma.io/gaupol/>`_ que j'ai installé à l'aide du
gestionnaire de paquets de ma distribution. Précisons que les modules de
la bibliothèque standard et ceux utilisés directement par ``pip`` sont omis
de la liste.

On constate également que chaque bibliothèque possède un *numéro de version*.

Numéros de version
------------------

Les numéros de version remplissent plusieurs rôles, mais l'un des principaux
est de spécifier des changements incompatibles.

Par exemple, pour ``cli-ui``, la façon d'appeler la fonction ``ask_choice``
a changé entre les versions 0.7 et 0.8, comme le montre cet extrait du
`changelog <https://tankerhq.github.io/python-cli-ui/changelog.html#v0-8-0)>`_ :

  *The list of choices used by ask_choice is now a named keyword argument:*

   .. code-block::

      # Old (<= 0.7)
      ask_choice("select a fruit", ["apple", "banana"])
      # New (>= 0.8)
      ask_choice("select a fruit", choices=["apple", "banana"])

Ceci s'appelle un *changement d'API*.

Réagir aux changements d'API
----------------------------

Plusieurs possibilités :

* On peut bien sûr adapter le code pour utiliser la nouvelle API, mais cela
  n'est pas toujours possible ni souhaitable.
* Une autre solution est de spécifier des *contraintes* sur le numéro de
  version dans la déclaration des dépendances. Par exemple : ::

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

Mais il y a un autre problème encore pire...

Conflit de dépendances
----------------------

Supposons deux projets A et B dans votre répertoire personnel. Ils dépendent
tous les deux de ``cli-ui``, mais l'un des deux utilise ``cli-ui 0.7`` et l'autre
``cli-ui 0.9``.  Que faire ?

Introduction
============


Importer un module
-------------------

Souvenez-vous, dans le chapitre 12 nous avons vu que le code suivant
Ce code fonctionne s'il y a un ficher `foo.py` quelque part qui contient la fonction
``bar``:::

    import foo
    foo.bar()


Ce fichier peut être présent soit dans le répertoire courant, soit dans la bibliothèque standard Python.

La variable PATH
-------------------

Vous connaissez peut-être le rôle de la variable d'environnement ``PATH``. Celle-ci contient une liste de chemins,
séparés par le caractère ``:`` et est utilisée par votre shell pour trouver le chemin complet des commandes que vous lancez.

Par exemple:

.. code-block:: console

  PATH="/bin:/usr/bin:/usr/sbin"
  $ ifconfig
  # lance le binaire /usr/sbin/ifconfig
  $ ls
  # lance le binaire /bin/ls

Le chemin est "résolu" par le shell en parcourant la liste de tout les
chemins de la variable `PATH`, et en regardant si le chemin complet
existe. La résolution s'arrête dès le premier chemin trouvé.

Par exemple, si vous avez ``PATH="/home/user/bin:/usr/bin"`` et un fichier ``ls`` dans ``/home/user/bin/ls``, c'est ce fichier-là
(et non ``/bin/ls``) qui sera utilisé quand vous taperez ``ls``.

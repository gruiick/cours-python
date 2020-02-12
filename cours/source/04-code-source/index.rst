Chapitre 4 - code source
========================

Non persistance des variables
------------------------------

.. code-block:: console

    $ python3
    >>> a = 2
    >>> quit()
    ```

.. code-block:: console

   $ python3
   >>> a
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   NameError: name 'a' is not defined


Du code dans un fichier
-----------------------

Aussi appelé: "code source", ou "source".

L'essence du logiciel libre :)



Installation d'un éditeur de texte simple
------------------------------------------

* Linux; ``gedit``, ``kate``, ...
* macOS: ``CotEditor``
* Windows: ``Notepad++``

J'insiste sur **simple**. Inutile d'installer un IDE pour le moment.


Configuration
-------------

* Police de caractères à chasse fixe
* Indentation de *4 espaces*
* Remplacer tabulation par des espaces
* Activer la coloration syntaxique



Notre premier fichier source
-----------------------------


Insérez le code suivant dans votre éditeur de texte

.. code-block:: python

   # Affiche un message
   print("Bonjour, monde")


Sauvegardez dans un fichier `bonjour.py` dans `Documents/e2l/python` par exemple


Lancer du code en ligne de commande
-----------------------------------


.. code-block:: console

   cd Documents/e2l/python/
   python3 bonjour.py
   Bonjour, monde

* Les lignes commençant par dièse (``#``) ont été ignorées - ce sont des *commentaires*.
* ``print()`` affiche la valeur, comme dans le REPL.


Note importante
---------------

Vous avez juste besoin:

* d'un éditeur de texte
* de Python3 installé
* d'une ligne de commande

Pas la peine d'installer quoique ce soit de plus pour le moment


1. *Recopiez* le code affiché dans votre éditeur, à la suite du code
   déjà écrit
2. Lancez le code depuis la ligne de commande
3. Réparez les erreurs éventuelles
4. Recommencez


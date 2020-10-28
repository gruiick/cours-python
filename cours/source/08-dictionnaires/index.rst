Chapitre 8 - Dictionnaires
==========================

Définition
----------

Un dictionaire est une *association* entre des clés et des valeurs.

* Les clés sont uniques
* Les valeurs sont arbitraires

Création de dictionnaires
-------------------------

Avec des accolades: ``{``, ``}`` ::

    dictionaire_vide =  {}

    une_clé_une_valeur = {"a": 42}

    deux_clés_deux_valeurs = {"a": 42, "b": 53}

Note: tous les dictionnaires sont truthy, sauf les dictionnaires vides.

Accès aux valeurs
------------------

Avec ``[]``, comme pour les listes, mais avec une *clé* à la place d'un *index*::

    scores = {"john": 10, "bob": 42}

    print(scores["john"])
    # affiche: 10

    print(scores["bob"])
    # affiche: 42

    print(scores["charlie"])
    # erreur: KeyError

Test d'appartenance
---------------------

Avec ``in``, comme le listes::

    scores = {"john": 10, "bob": 42}
    print("charlie" in scores)
    # affiche: False

Modifier la valeur d'une clé
-----------------------------

Comme pour les listes, avec une assignation::

    scores = {"john": 10, "bob": 42}
    scores["john"] = 20
    print(scores)
    # affiche: {"john": 20, "bob": 42}

Créer une nouvelle clé
-----------------------

Même mécanisme que pour la modification des clés existantes::

    scores = {"john": 10, "bob": 42}
    scores["charlie"] = 30
    print(scores)
    # affiche: {"john": 20, "bob": 42, "charlie": 30}

*rappel*: ceci ne fonctionne pas avec les listes: on ne peut
pas "créer" de nouveaux éléments dans la liste juste
avec un index::

    ma_liste = ["a", "b"]
    ma_liste[1] = "c"
    print(ma_liste)
    # affiche: ["a", "c"]

    ma_liste[3] = "d"
    # erreur: IndexError

Itérer sur les clés
-------------------

Avec ``for ... in ...``, comme pour les listes::

    scores = {"john": 10, "bob": 42}
    for nom in scores:
    	# on assigne la valeur "john" à la variable `nom`, puis "bob"
    	score_associé_au_nom = scores[nom]
        # on assigne la valeur 10 puis la valeur 42 à la variable
        # score_associé_au_nom
    	print(nom, score_associé_au_nom)

.. code-block::

    john 10
    bob 42

del
---

Détruire une clé
+++++++++++++++++

Avec ``del`` - un nouveau mot-clé::

    scores = {"john": 10, "bob": 42}
    del scores["bob"]
    print(scores)
    # affiche: {"john": 10}

Détruire un élément d'une liste
++++++++++++++++++++++++++++++++

Aussi avec ``del``::

    fruits = ["pomme", "banane", "poire"]
    del fruits[1]
    print(fruits)
    # affiche: ["pomme", "poire"]

Détruire une variable
+++++++++++++++++++++

Encore et toujours ``del``::

    mon_entier = 42
    mon_entier += 3
    print(mon_entier)
    # affiche: 45

    del mon_entier
    mon_entier += 1
    # erreur: NameError


Comparaisons de dictionaires
-----------------------------

Deux dictionaires sont considérés égaux s'ils ont les mêmes clés
et les mêmes valeurs. L'ordre n'importe pas::

    {"a":1, "b":2} == {"a":1, "b":2}  # True
    {"a":1, "b":2} == {"b":2, "a":1}  # True
    {"a":1, "b":2} == {"a":1, "b":3}  # False


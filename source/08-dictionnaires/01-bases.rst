Principes fondamentaux
======================

Définition
----------

Un dictionnaire est une *association* entre des clés et des valeurs.

* les clés sont uniques ;
* les valeurs sont arbitraires.

Création de dictionnaires
-------------------------

Les dictionnaires sont créés avec des accolades: ``{``, ``}`` : ::

    dictionnaire_vide =  {}

Ensuite, on utilise ``:`` pour séparer la clé et la valeur. Enfin, les paires de clé/valeur sont séparées par des virgules ``,`` : ::

    une_clé_une_valeur = {"a": 42}

    deux_clés_deux_valeurs = {"a": 42, "b": 53}


Accès aux valeurs
-----------------

Avec ``[]``, comme pour les listes, mais avec une *clé* à la place d'un *index* : ::

    scores = {"john": 10, "bob": 42}

    print(scores["john"])
    # affiche: 10

    print(scores["bob"])
    # affiche: 42

    print(scores["charlie"])
    # erreur: KeyError


Modifier la valeur d'une clé
----------------------------

Comme pour les listes, avec une assignation : ::

    scores = {"john": 10, "bob": 42}
    scores["john"] = 20
    print(scores)
    # affiche: {"john": 20, "bob": 42}

Créer une nouvelle clé
----------------------

Même mécanisme que pour la modification des clés existantes : ::

    scores = {"john": 10, "bob": 42}
    scores["charlie"] = 30
    print(scores)
    # affiche: {"john": 20, "bob": 42, "charlie": 30}

*rappel* : Ceci ne fonctionne pas avec les listes. On ne peut
pas "créer" de nouveaux éléments dans la liste juste
avec un index : ::

    ma_liste = ["a", "b"]
    ma_liste[1] = "c"
    print(ma_liste)
    # affiche: ["a", "c"]

    ma_liste[3] = "d"
    # erreur: IndexError

del
---

Détruire une clé
++++++++++++++++

Avec ``del`` - un nouveau mot-clé : ::

    scores = {"john": 10, "bob": 42}
    del scores["bob"]
    print(scores)
    # affiche: {"john": 10}

Détruire un élément d'une liste
+++++++++++++++++++++++++++++++

Aussi avec ``del`` : ::

    fruits = ["pomme", "banane", "poire"]
    del fruits[1]
    print(fruits)
    # affiche: ["pomme", "poire"]

Détruire une variable
+++++++++++++++++++++

Encore et toujours ``del`` : ::

    mon_entier = 42
    mon_entier += 3
    print(mon_entier)
    # affiche: 45

    del mon_entier
    mon_entier += 1
    # erreur: NameError



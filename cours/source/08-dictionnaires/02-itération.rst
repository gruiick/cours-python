Itération et dictionaires
==========================

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


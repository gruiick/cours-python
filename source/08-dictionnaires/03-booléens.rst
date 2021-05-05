Dictionnaires et booléens
=========================

Falsy et truthy
----------------

Les dictionnaires vides sont falsy, et tous les autres dictionnaires sont truthy::

   mon_dico = {"a": 1, "b": 2}
   if mon_dico:
       print("mon_dico est truthy")
   else:
       print("mon_dico est falsy")
   # affiche: mon_dico est truthy

   mon_autre_dico = {}
   if mon_autre_dico:
       print("mon_autre_dico n'est pas vide")
   else:
       print("mon_autre_dico est vide")
   # affiche: mon_autre_dico est vide

Test d'appartenance
---------------------

On peut vérifier si une clé est présente dans un dictionnaires avec
le mot clé ``in``, un peu comme pour le listes::

    scores = {"john": 10, "bob": 42}
    print("john" in scores)
    # affiche: True

    print("charlie" in scores)
    # affiche: False



Comparaisons de dictionnaires
-----------------------------

Deux dictionnaires sont considérés égaux s'ils ont les mêmes clés
et les mêmes valeurs. L'ordre n'importe pas::

    {"a":1, "b":2} == {"a":1, "b":2}  # True
    {"a":1, "b":2} == {"b":2, "a":1}  # True
    {"a":1, "b":2} == {"a":1, "b":3}  # False


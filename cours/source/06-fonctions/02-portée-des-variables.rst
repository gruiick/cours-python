Portée des variables
====================

Les arguments d'une fonction n'existent que dans le corps de celle-ci::

    def dire_bonjour(prénom):
    	print("Bonjour " + prénom)

    dire_bonjour("Dimitri") # Ok
    print(prénom)  # Erreur


Les variables en dehors des fonctions sont disponibles partout::

    salutation = "Bonjour "

    def dire_bonjour(prénom):
    	print(salutation + prénom)

    dire_bonjour("Dimitri")

Une variable peut avoir en "cacher" une autre si elle a une portée différente::

    def dire_bonjour(prénom):
    	print("Bonjour " + prénom)   # portée: uniquement dans
    								 # le corps dire_bonjour

    prénom = "Dimitri"  # portée: dans tout le programme
    dire_bonjour(prénom) # Ok

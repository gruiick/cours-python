Valeur de retour d'une fonction
=================================

Définition avec le mot ``return``::

    def additionner(x, y):
    	return x + y

Récupérer la valeur de retour::

   a = 3
   b = 4
   c = additionner(a, b)   # encore une assignation
   print(c)
   # Affche: 7

Sortir d'une fonction avec return
---------------------------------

``return`` interrompt également l'éxécution du
corps de la fonction::

    def dire_bonjour(prénom, première_fois=False):
    	print("Bonjour", prénom)
    	if not première_fois:
    		return
    	print("Heureux de faire votre connaissance")

    >>> dire_bonjour("Dimitri", première_fois=True)
    Bonjour Dimitri
    Heureux de faire votre connaissance

    >>> dire_bonjour("Dimitri", première_fois=False)
    Bonjour Dimitri

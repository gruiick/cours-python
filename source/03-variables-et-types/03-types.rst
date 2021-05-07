Types
=====

On a vu qu'on pouvait utiliser ``+`` **à la fois** pour additionner des nombres
ou concaténer des strings. Mais on ne peut pas utiliser ``+`` avec une string
d'un côté et un entier de l'autre : ::

   a = 42
   b = 4
   c = a + b  # ok

   salutation = "bonjour, "
   prénom = "Bob"
   salutation + prénom  # ok

   résultat = a + prénom
   # affiche:
   # TypeError: can only concatenate str (not "int") to str


Ceci est notre premier message d'erreur : si l'interpréteur est incapable
d'exécuter une instruction, il affiche un message d'erreur et s'interrompt
immédiatement.


Conversions
-----------

Pour résoudre le problème ci-dessus, il faut effectuer une *conversion de types* :

Entier vers string
++++++++++++++++++

On peut convertir un entier en string en utilisant le mot ``str`` et des parenthèses
autour de l'expression : ::

    x = 40
    y = 2
    message = "La réponse est: " + str(x + y)
    print(message)
    # affiche: La réponse est 42



String vers nombres
+++++++++++++++++++

Inversement, on peut convertir un string en entier en utilisant
le mot ``int`` et des parenthèses : ::


   quarante_en_chiffres = "40"
   réponse = int(quarante_en_chiffres) + 2
   print(réponse)
   # affiche: 42

Pour convertir une string en flottant, on peut utiliser ``float()`` : ::

    taille_sur_le_passeport = "1.62"
    taille_en_mètres = float(taille_sur_le_passeport)



Fonctions à plusieurs arguments
===============================

On peut mettre autant d'arguments qu'on veut, séparés
par des virgules::

    def soustraction(x, y):
        résultat = x - y
        return résultat

    résultat = soustraction(5, 4)
    print(résultat)
    # affiche: 1

Arguments nommés
----------------

En Python, on peut aussi utiliser le *nom* des arguments au lieu de
leur position::

    def dire_bonjour(prénom):
        print("Bonjour " + prénom)

    dire_bonjour(prénom="Gertrude")
    # Affiche: Bonjour Gertrude

    résultat = soustraction(y=4, x=5)
    print(résultat)
    # affiche: 1

Valeur de retour d'une fonction
=================================

On peut également appeler une fonction dans une expression
à droite d'une assignation de variable.

Dans ce cas, la valeur de l'expression est obtenue en
exécutant le corps de la fonction jusqu'à rencontrer l'instruction
`return` et en évaluant l'expression à droite du return.

Par exemple::

    def retourne_42():
        return 42

    x = retourne_42()
    print(x)
    # Affiche: 42

Ici, on peut dire que `42` est le *résultat* de l'appel de la fonction `retourne_42()`.

On peut utiliser `if` avec plusieurs `return` pour changer le résultat d'une fonction::

    def peut_conduire(âge):
        if âge < 18:
            return False
        else:
            return True

    x = peut_conduire(16)
    print(x)
    # Affiche: False

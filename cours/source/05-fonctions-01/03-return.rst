Valeur de retour d'une fonction
=================================

On peut également appeler une fonction dans une expression
à droite d'une assignation de variable.

Dans ce cas, la valeur de l'expression est obtenue en
éxécutant le corps de la fonction jusqu'à rencontrer l'instruction
`return` et en évaluant l'expression à droite du return.

Par exemple::

    def retourne_42():
        return 42

    x = retourne_42()
    print(x)
    # Affiche: 42

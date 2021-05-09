pass
====


À cause de l'organisation du flot de contrôle en blocs indentés, on ne
peut pas vraiment avoir de blocs vides. Mais parfois, on a besoin d'un bloc
qui ne fasse rien - c'est là que le mot-clé ``pass`` rentre en jeu.

``pass`` représente une instruction qui ne fait rien.

Un exemple : ::

    une_condition = False
    if une_condition:
        pass
    else:
        print("une_condition n'est pas vraie")

On peut aussi - et c'est l'usage le plus courant - utiliser ``pass`` pour
définir une fonction qui ne fait rien : ::

    def ne_fait_rien():
        pass



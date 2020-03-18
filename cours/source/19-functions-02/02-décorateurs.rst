Fonctions en tant qu'argement d'autres fonctions
================================================

On a vu en début de chapitre qu'on peut créé des variables qui pointent
vers des fonctions.

Du coup, rien n'empêche de les passer en *argument* d'autres fonctions.

Par exemple::

    def appelle_deux_fois(f):
        f()
        f()


    def crier():
        print("Aline !")

    appelle_deux_fois(crier)

    # Affiche:
    # Aline !
    # Aline !

Arguments par défaut
====================

On peut aussi mettre des valeurs par défaut : ::

    def dire_bonjour(prénom, enthousiaste=False):
        message = "Bonjour " + prénom
        if enthousiaste:
            message += "!"
        print(message)

Appel : ::

    dire_bonjour("Thomas")
    # affiche: Bonjour Thomas

    dire_bonjour("Thomas", enthousiaste=True)
    # affiche: Bonjour Thomas!

    dire_bonjour("Thomas", enthousiaste=False)
    # affiche: Bonjour Thomas


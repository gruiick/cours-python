import random


class Robot:
    def __init__(self):
        self._nom = None
        self._éteint = True

    def nom(self):
        nom = self._nom
        return nom

    def démarre(self):
        if self._nom is None:
            self._nom = faire_un_nom()
        else:
            pass
        self._éteint = False

    def éteint(self):
        self._éteint = True

    def réinitialise(self):
        self._nom = None


def main():
    robot = Robot()
    print("Le premier robot n'a pas encore de nom")
    print("La ligne suivante doit afficher None")
    print("01", robot.nom())

    print("On démarre le premier robot")
    robot.démarre()
    print("Le permier robot a maintenan un nom")
    print("La ligne suivante doit afficher un nom au hasard")
    print("02", robot.nom())

    print("Le nom ne change pas tant que le robot n'est pas re-initialisé")
    print("La ligne suivante doit afficher le même nom que la ligne 02")
    robot.éteint()
    robot.démarre()
    print("03", robot.nom())

    print("Le nom est effacé quand on réinitialise le robot")
    print("La ligne suivante doit afficher None")
    robot.réinitialise()
    print("04", robot.nom())

    print("Un nouveau nom est généré quand on re-démarre le robot")
    print("La ligne suivante doit afficher un nom différent de la ligne 03")
    robot.démarre()
    print("05", robot.nom())


def donne_lettre_au_hasard():
    index = random.randint(0, 25)
    liste_de_lettres = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    lettre = liste_de_lettres[index]
    return lettre


def donne_chiffre_au_hasard():
    index = random.randint(0, 9)
    liste_de_chiffres = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    liste_de_chiffres = "1234567890"
    chiffre = liste_de_chiffres[index]
    return chiffre


def faire_un_nom():
    nom = (
        donne_lettre_au_hasard()
        + donne_lettre_au_hasard()
        + donne_chiffre_au_hasard()
        + donne_chiffre_au_hasard()
        + donne_chiffre_au_hasard()
    )
    return nom


main()

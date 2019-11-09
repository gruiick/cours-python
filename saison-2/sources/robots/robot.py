class Robot:
    pass


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



main()


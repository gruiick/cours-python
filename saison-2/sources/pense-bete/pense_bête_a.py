def parse(entrée_utilisateur):
    premiere_lettre = entrée_utilisateur[0]
    if premiere_lettre == "+":
        return ("ajouter", entrée_utilisateur[2:])
    elif premiere_lettre == "-":
        return ("supprimer", int(entrée_utilisateur[2:]))
    elif premiere_lettre == "x":
        return ("marquer_fait", int(entrée_utilisateur[2:]))
    elif premiere_lettre == "o":
        return ("marquer_non_fait", int(entrée_utilisateur[2:]))
    elif premiere_lettre == "q":
        return ("quitter", None)


class ChoseAfaire:
    def __init__(self, contenu: str, fait: bool):
        self.contenu = contenu
        self.fait = fait


class PenseBete:
    # index commence à 1!
    def __init__(self):
        self.liste = []

    def ajouter(self, chose_à_faire):
        self.liste.append(chose_à_faire)

    def supprimer(self, index):
        del self.liste[index - 1]

    def marquer_fait(self, index):
        self.liste[index - 1].fait = True

    def marquer_non_fait(self, index):
        self.liste[index - 1].fait = False

    def afficher(self):
        for chose_à_faire in self.liste:
            if chose_à_faire.fait == True:
                print("[x]", chose_à_faire.contenu)
            else:
                print("[ ]", chose_à_faire.contenu)


def main():
    pense_bete = PenseBete()
    while True:
        pense_bete.afficher()
        entrée_utilisateur = input()
        action, argument = parse(entrée_utilisateur)
        if action == "ajouter":
            chose_à_faire = ChoseAfaire(argument, False)
            pense_bete.ajouter(chose_à_faire)
        elif action == "supprimer":
            pense_bete.supprimer(argument)
        elif action == "marquer_fait":
            pense_bete.marquer_fait(argument)
        elif action == "marquer_non_fait":
            pense_bete.marquer_non_fait(argument)
        elif action == "quitter":
            break


main()

class ChosesÀFaire:
    def __init__(self, contenu, fait):
        self.contenu = contenu
        self.fait = fait


class PenseBête:
    def __init__(self):
        self.liste = []

    def ajouter(self, choses_à_faire):
        self.liste.append(choses_à_faire)

    def supprimer(self, index):
        del self.liste[index - 1]

    def marquer_fait(self, index: int):
        self.liste[index - 1].fait = True

    def marquer_non_fait(self, index: int):
        self.liste[index - 1].fait = False

    def affiche(self):
        if len(self.liste):
            for i in range(len(self.liste)):
                marque = ""
                if not self.liste[i].fait:
                    marque = "x"
                print(str(i + 1) + " [" + marque + "] " + self.liste[i].contenu)
        else:
            print("[]")


def parse(entrée_utilisateur):
    if entrée_utilisateur != "q":
        e = entrée_utilisateur.split()
        action = e.pop(0)
        argument = " ".join(e)
        dico = {
            "+": "ajouter",
            "-": "supprimer",
            "o": "marquer_fait",
            "x": "marquer_non_fait",
        }
        try:
            if argument.isdigit():
                argument = int(argument)
            return dico[action], argument
        except:
            return "erreur", "message d'erreur"
    else:
        return "quitter", None
    # return ("ajouter", contenu)
    # return ("supprimer", index)
    # return ("marquer_fait", index)
    # return ("marquer_non_fait", index)
    # return ("erreur", message)
    # return ("quitter", None)


def main():
    pense_bête = PenseBête()
    while True:
        entrée_utilisateur = input()
        action, argument = parse(entrée_utilisateur)
        if action == "ajouter":
            chose_à_faire = ChosesÀFaire(argument, True)
            pense_bête.ajouter(chose_à_faire)
        elif action == "supprimer":
            pense_bête.supprimer(argument)
        elif action == "marquer_fait":
            pense_bête.marquer_fait(argument)
        elif action == "marquer_non_fait":
            pense_bête.marquer_non_fait(argument)
        elif action == "erreur":
            print(argument)
        else:
            pense_bête.affiche()
            break
        pense_bête.affiche()


main()

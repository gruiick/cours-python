import sys


def lire_code():
    if len(sys.argv) < 2:
        print(
            "Pas assez d'arguments",
            file=sys.stderr
        )
        sys.exit(1)
    return sys.argv[1].upper()

def fabrique_dico():
    dico = dict()
    file = open("airports.txt", "r")
    contenu = file.read()
    lignes = contenu.splitlines()
    for ligne in lignes:
        code = ligne[0:3]
        nom = ligne[4:]
        dico[code] = nom
    return dico


def trouve_code(code, dico):
    if code in dico:
        return dico[code]


def affiche_erreur(code):
    print(
        "Code:", code,
        "non trouvé",
        file=sys.stderr
    )
    sys.exit(2)


def main():
    dico = fabrique_dico()
    code = lire_code()
    nom = trouve_code(code, dico)
    if nom:
        print(nom)
    else:
        affiche_erreur(code)


main()

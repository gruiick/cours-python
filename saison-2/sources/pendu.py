import random


def choisir_mot_au_hasard():
    fichier = open("mots.txt")
    contenu = fichier.read()
    fichier.close()
    mots = contenu.splitlines()
    n = len(mots)
    index = random.randint(0, n - 1)
    return mots[index]


def main():
    mot = choisir_mot_au_hasard()
    # pour debuggage
    # print(mot)
    tentatives = []
    while True:
        afficher_indice(mot, tentatives)
        lettre = demander_lettre()
        tentatives += [lettre]
        if a_gagné(mot, tentatives):
            print("Gagné")
            print(mot)
            break


def a_gagné(mot, tentatives):
    for c in mot:
        if c not in tentatives:
            return False
    return True


def demander_lettre():
    print("entrer une lettre")
    lettre = input()
    return lettre


def afficher_indice(mot, tentatives):
    for c in mot:
        if c in tentatives:
            print(c, end="")
        else:
            print("_", end="")
    print()


main()

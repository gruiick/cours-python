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
    print(mot)


main()

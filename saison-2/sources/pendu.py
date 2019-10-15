import random

import json


def lire_scores():
    with open("scores.json") as f:
        scores = json.load(f)
        return scores


def enregistrer_scores(scores):
    with open("scores.json", "w") as f:
        scores = json.dump(scores, f, indent=2)
        return scores


def choisir_mot_au_hasard():
    fichier = open("mots.txt")
    contenu = fichier.read()
    fichier.close()
    mots = contenu.splitlines()
    n = len(mots)
    index = random.randint(0, n - 1)
    return mots[index]


def demander_joueur():
    joueur = input("donnez votre nom: ")
    return joueur


def jeu():
    mot = choisir_mot_au_hasard()
    print(mot)
    tentatives = []
    while True:
        afficher_indice(mot, tentatives)
        lettre = demander_lettre()
        tentatives += [lettre]
        score = len(tentatives)
        if a_gagné(mot, tentatives):
            print("Gagné")
            print(mot)
            return score


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


def ajouter_resultat(scores, joueur_courant, score_courant):
    record = None
    for nom in scores:
        score = scores[nom]
        if record is None:
            record = score
        elif score < record:
            record = score
    if record is None:
        record = score_courant
        print(joueur_courant + ", vous avez établi le record à ", record)
    elif score_courant < record:
        print(joueur_courant + ", vous avez battu le record de ", record)
    scores[joueur_courant] = record
    return scores


# main()

anciens_scores = {"Bob": 30}
joueur_courant = "Alice"
score_courant = 28

nouveaux_scores = ajouter_resultat(anciens_scores, joueur_courant, score_courant)
print(nouveaux_scores)

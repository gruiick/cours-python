#
# dessiner un sapin


def demander_largeur():
    largeur = input("Veuillez entrer une valeur : ")
    largeur_totale = int(largeur)
    return largeur_totale


def suite_arithmetique(largeur):
    liste_des_largeurs = [1]
    i = 0
    while i < largeur // 2 - 1:
        liste_des_largeurs += [liste_des_largeurs[i] + 2]
        i = i + 1
    return liste_des_largeurs


def imprime_ligne(nombre_blancs, largeur_courante):
    print(" " * nombre_blancs, end="")
    print("#" * largeur_courante)


def imprime_houppier(liste_des_largeurs, largeur_totale):
    for largeur_courante in liste_des_largeurs:
        nombre_blancs = (largeur_totale - largeur_courante) // 2
        imprime_ligne(nombre_blancs, largeur_courante)


def main():
    largeur_totale = demander_largeur()
    liste_des_largeurs = suite_arithmetique(largeur_totale)
    imprime_houppier(liste_des_largeurs, largeur_totale)


main()

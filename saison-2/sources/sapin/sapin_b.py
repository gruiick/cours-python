def largeur():
    n = int(input("donnez une larguer impaire = "))
    return n


def affiche_sapin(largeur_totale):
    index = int((largeur_totale - 1) / 2)
    for index_courant in range(index + 1):
        largeur_courante = (index_courant * 2) + 1
        affiche_ligne(index_courant, largeur_courante, largeur_totale)
    largeur_pied = int(largeur_totale / 3)
    affiche_ligne(0, 1, largeur_totale)
    affiche_ligne(0, 1, largeur_totale)


def affiche_ligne(index_courant, largeur_courante, largeur_totale):
    nbr_blanc = int(largeur_totale / 2) - index_courant
    blanc = " " * nbr_blanc
    print(blanc, "#" * largeur_courante, blanc, sep="")


def main():
    largeur_totale = largeur()
    affiche_sapin(largeur_totale)


main()

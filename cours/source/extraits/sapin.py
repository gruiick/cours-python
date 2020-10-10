largeur = 10


def affiche_ligne(début, fin):
    blancs_au_début = " " * début
    largeur_ligne = fin - début
    dièses = "#" * largeur_ligne
    print(blancs_au_début + dièses)


def affiche_feuilles():
    affiche_ligne(5, 6)
    affiche_ligne(4, 7)
    # à compléter


def affiche_pied():
    affiche_ligne(5, 6)
    # à compléter


def affiche_sapin():
    affiche_feuilles()
    affiche_pied()


affiche_sapin()

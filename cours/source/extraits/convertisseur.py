import sys


def trouver_coefficient(unité):
    return 1.0


def conversion_en_mètres(valeur, unité_de_départ):
    coefficient = trouver_coefficient(unité_de_départ)
    return valeur * coefficient


def conversion_depuis_mètres(valeur, unité_d_arrivée):
    return 1.0


def convertir(valeur, unité_de_départ, unité_d_arrivée):
    print("Conversion de", valeur, "en", unité_de_départ, "vers", unité_d_arrivée)
    en_mètres = conversion_en_mètres(valeur, unité_de_départ)
    résultat = conversion_depuis_mètres(en_mètres, unité_d_arrivée)
    return résultat


def main():
    nombre_arguments = len(sys.argv) - 1
    if nombre_arguments != 3:
        print("3 arguments attendus, mais", nombre_arguments, "reçu(s)")
        return
    valeur = float(sys.argv[1])
    unité_de_départ = sys.argv[2]
    unité_d_arrivée = sys.argv[3]
    valeur_de_sortie = convertir(valeur, unité_de_départ, unité_d_arrivée)
    print(f"{valeur_de_sortie:.6}")


main()

import numpy
from matplotlib import pyplot
import sys

# list_abscisses = [0, 1, 2, 3]
# list_ordonnées = [0, 3, 6, -2]

# list_abscisses = []
# list_ordonnées = []


def calcul_suite(const, nb_inter):
    list_abscisses = range(0, nb_inter)
    x = 0.5
    list_ordonnées = []
    for i in list_abscisses:
        list_ordonnées.append(x)
        x = const * x * (1 - x)
    return (list_abscisses, list_ordonnées)


def main():
    const = sys.argv[1]
    const = float(const)
    resultat_calcul = calcul_suite(const, 500)
    list_abscisses = resultat_calcul[0]
    list_ordonnées = resultat_calcul[1]
    pyplot.plot(list_abscisses, list_ordonnées)
    pyplot.show()


main()

# commandes à lancer
# ./.venv/bin/python3 suite.py 2
# ./.venv/bin/python3 suite.py 3
# ./.venv/bin/python3 suite.py 3.05
# ./.venv/bin/python3 suite.py 3.58
# ./.venv/bin/python3 suite.py 3.58

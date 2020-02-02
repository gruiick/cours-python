from matplotlib import pyplot
import numpy
import sys

k = float(sys.argv[1])

def f(x):
    return k * x * (1-x)

x0 = 0.5

n = 200

def liste(n):
    resultat = [x0]
    for i in range(n):
        resultat.append(f(resultat[-1]))
    return resultat


abscisses = list(numpy.linspace(0, 10, n+1))
ordonnées = liste(n)

pyplot.plot(abscisses, ordonnées)
pyplot.show()
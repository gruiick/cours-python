import numpy
from matplotlib import pyplot
import sys

ITERATIONS = 1000


def suite(initial, k):
    ts = numpy.linspace(0, 1, ITERATIONS)
    x = initial
    vs = []
    for i in ts:
        vs.append(x)
        x = x * k * (1 - x)
    return (ts, vs)


def main():
    k = float(sys.argv[1])
    # 1.2 ou 2.8 ou 3.5 ou 3.86
    ts, vs = suite(0.5, k)
    ts, vs2 = suite(0.4, k)
    pyplot.plot(ts, vs)
    pyplot.plot(ts, vs2)
    pyplot.show()


main()

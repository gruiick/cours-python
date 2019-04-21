import sys


def convert(value, unit_in, unit_out):
    coefficient = get_coefficient(unit_in, unit_out)
    return value * coefficient


def get_coefficient(unit_in, unit_out):
    distances = {"km": 1 / 1000, "miles": 1 / 1609, "m": 1}

    reciprocal_coefficient = 1 / distances[unit_in]

    return distances[unit_out] * reciprocal_coefficient


def main():
    try:
        value = sys.argv[1]
        unit_in = sys.argv[2]
        unit_out = sys.argv[3]

    except IndexError:
        print("Pas assez d'arguments")
        sys.exit(1)

    try:
        value = float(value)
    except ValueError:
        print("Le premier argument doit être un nombre")
        sys.exit(1)

    result = convert(value, unit_in, unit_out)
    print(f"{result:.2f}")


if __name__ == "__main__":
    main()

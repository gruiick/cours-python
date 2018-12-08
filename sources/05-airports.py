import sys


def build_airport_dict():
    result = dict()
    file = open("airports.txt", "r")
    contents = file.read()
    lines = contents.splitlines()
    for line in lines:
        words = line.split(" ", maxsplit=1)
        assert len(words) == 2
        code = words[0]
        name = words[1].strip()
        result[code] = name
    return result


def main():
    if len(sys.argv) < 2:
        sys.exit("Not enough arguments")

    airport_dict = build_airport_dict()
    code = sys.argv[1]
    if code not in airport_dict:
        sys.exit("Code not found")
    result = airport_dict[code]
    print(result)


main()

import sys


def get_value(pair):
    key, value = pair
    return value


def get_word(chunk):
    if all(x.isalpha() for x in chunk):
        if len(chunk) < 4:
            return None
        return chunk.lower()
    else:
        return None


def main():
    filename = sys.argv[1]
    stream = open(filename, "r")

    scores = {}

    for line in stream.readlines():
        for chunk in line.split():
            word = get_word(chunk)
            if word:
                if not word in scores:
                    scores[word] = 0
                else:
                    scores[word] += 1

    stream.close()


if __name__ == "__main__":
    main()

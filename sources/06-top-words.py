import sys


def get_value(pair):
    key, value = pair
    return value


def get_word(chunk):
    if all(x.isalpha() for x in chunk):  # is_alpha()
        if len(chunk) < 4:
            return None
        return chunk.lower()  # lower()
    else:
        return None


def main():
    filename = sys.argv[1]
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    scores = {}

    for line in lines:
        for chunk in line.split():
            word = get_word(chunk)
            if word:
                if not word in scores:
                    scores[word] = 1
                else:
                    scores[word] += 1

    to_sort = []
    for k in scores:   # iterate on dicts
        v = scores[k]
        to_sort.append([v, k])
    to_sort.sort()


    print(to_sort[-10:])


main()

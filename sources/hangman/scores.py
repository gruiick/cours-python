def parse_scores():
    res = dict()
    with open("scores.txt") as file:
        for line in file.readlines():
            name, score = line.split()
            res[name] = int(score)
    return res


def main():
    scores = parse_scores()
    for name, score in scores.items():
        print(name, score)


main()

def parse_scores():
    res = dict()
    with open("scores.txt") as file:
        for line in file.readlines():
            name, score = line.split()
            res[name] = int(score)
    return res


def print_scores(scores):
    print("Tableau des résultats:")
    for name, score in scores.items():
        print(name, score)


def register_score(scores, name, new_score):
    pass


def main():
    scores = parse_scores()
    name = input("nom: ")
    new_score = input("score: ")
    register_score(scores, name, new_score)
    print_scores(scores)


main()

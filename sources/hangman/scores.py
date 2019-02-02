def parse_scores():
    res = dict()
    with open("scores.txt") as file:
        for line in file.readlines():
            name, score = line.split()
            res[name] = int(score)
    return res

scores = { "joe" : 42, "jack" : 43 }

print (convert(scores))


def print_scores(scores):
    print("Tableau des résultats:")
    for name, score in scores.items():
        print(name, score)

def convert(scores):
    res = ""
    for name, score in scores.items():
        res += name + " " + str(score) + "\n"
    return res


def register_score(scores, name, new_score):
    # Mise à jour des tableaux des scores
    # Et écriture dans un fichier
    scores[name] = new_score
    
    with open("scores.txt", "w") as file:
        file.write(convert(scores))
    
    
def main():
    scores = parse_scores()
    name = input("nom: ")
    new_score = input("score: ")
    register_score(scores, name, new_score)
    print_scores(scores)


main()    

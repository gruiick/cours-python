import random

nombre_secret = random.randint(0, 100)

print("devine le nombre auquel je pense entre 0 et 100")
entrée_utilisateur = int(input())

while True:
    if entrée_utilisateur == nombre_secret:
        print("bravo")
        break
    else:
        print("mauvaise réponse")
        entrée_utilisateur = int(input())

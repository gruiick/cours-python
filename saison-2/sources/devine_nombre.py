import random

nombre = random.randint(0, 100)
print("devine le nombre auquel je pense")


while True:
    nombre_devine = int(input())
    if nombre_devine > nombre:
        print("trop grand")
    elif nombre_devine < nombre:
        print("trop petit")
    else:
        print("bravo")
        break

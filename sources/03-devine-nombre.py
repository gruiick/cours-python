import random

secret = random.randint(0, 100)

print("Devine le nombre auquel je pense")
while True:
    response = input()
    response = int(response)
    if response > secret:
        print("Trop grand")
        continue
    if response < secret:
        print("Trop petit")
        continue
    print("Gagné")
    break

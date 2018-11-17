import random

secret = random.randint(0, 100)

print("Devine le nombre auquel je pense")
while True:
    response = input()
    response = int(response)

    if response == secret:
        print("Gagné")
        break
    else:
        if response > secret:
            print("Trop grand")
        if response < secret:
            print("Trop petit")

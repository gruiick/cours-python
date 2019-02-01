import sys
import random


def read_words():
    file = open("words.txt")
    contents = file.read()
    file.close()
    words = contents.splitlines()
    return words


def choose_word(words):
    n = len(words)
    index = random.randint(0, n - 1)
    return words[index]


def has_won(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    return True


def display_hint(word, letters):
    for letter in word:
        if letter in letters:
            print(letter, end="")
        else:
            print("_", end="")
    print("")


def main():
    num_tries = 10
    words = read_words()
    word = choose_word(words)

    letters = set()
    display_hint(word, letters)

    while num_tries:
        print(num_tries, "essai(s) restant(s)")

        answer = input()
        while answer in letters:
            print("Lettre déjà proposée")
            answer = input()

        if len(answer) == len(word):
            guess = answer
            if guess == word:
                print("Gagné")
                sys.exit(0)
            else:
                print("Mauvaise réponse")
                num_tries -= 1

        elif len(answer) == 1:
            letter = answer
            letters.add(letter)
            display_hint(word, letters)
            if has_won(word, letters):
                print("Gagné")
                sys.exit(0)
            else:
                num_tries -= 1

        else:
            print("Veuillez entrer juste une lettre ou le mot entier")

    print("Vous avez dépassé le nombre d'essais autorisés")
    print("Le mot à deviner était :", word)
    sys.exit(1)



main()

import random

def read_words():
    stream = open("noms.txt")
    words = stream.read().splitlines()
    stream.close()
    return words


def choose_word(words):
    n = len(words)
    index = random.randint(0, n-1)
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
    words = read_words()
    word = choose_word(words)
    print(word)

    letters = set()
    display_hint(word, letters)

    while True:
        new_letter = input()
        letters.add(new_letter)
        display_hint(word, letters)
        if has_won(word, letters):
            print("Gagné")
            return


if __name__ == "__main__":
    main()

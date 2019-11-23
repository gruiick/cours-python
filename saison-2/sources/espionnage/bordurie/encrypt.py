import sys


def rotate(x, y):
    return (x + y) % 26


def shift(letter, n):
    x = ord(letter) - ord("A")
    y = rotate(x, n)
    return chr(ord("A") + y)


def rot13(message):
    message = "".join([x for x in message if x.isalpha()])
    message = message.upper()
    res = ""
    for c in message:
        res += shift(c, 13)
    return res


def encrypt(key, message):
    message = "".join([x for x in message if x.isalpha()])
    message = message.upper()
    res = ""
    i = 0
    for c in message:
        x = ord(key[i % len(key)]) - ord("A")
        res += shift(c, x)
        i += 1
    return res


def main():
    cle = sys.argv[1]
    message = sys.argv[2]
    res = encrypt(cle, message)
    print(res)


if __name__ == "__main__":
    main()

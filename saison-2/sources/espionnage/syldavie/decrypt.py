import sys
import string


def rotate(x, y):
    return (x - y) % 26


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


def decrypt(key, message):
    message = "".join([x for x in message if x.isalpha()])
    message = message.upper()
    res = ""
    i = 0
    for c in message:
        x = ord(key[i % len(key)]) - ord("A")
        res += shift(c, x)
        i += 1
    return res


def try_with_key(key, message):
    res = decrypt(key, message)
    if "PLEKSZYGLADZ" in res:
        return res


def main():
    message = sys.argv[1]
    print(decrypt('N', message))

    """
    message = sys.argv[1]
    letters = string.ascii_uppercase
    for a in letters:
        for b in letters:
            for c in letters:
                key = a + b + c
                res = try_with_key(key, message)
                if res:
                    print(res)
                    print("key:", key)
                    return
                    """


if __name__ == "__main__":
    main()

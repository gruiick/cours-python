def rotate(x, y):
    return (x + y) % 26


def shift(letter, n):
    x = ord(letter) - ord('A')
    y = rotate(x, n)
    return chr(ord('A') + y)


def rot13(message):
    message = "".join([x for x in message if x.isalpha()])
    message = message.upper()
    res = ""
    for c in message:
        res += shift(c, 13)
    return res


def test_rotate():
    assert rotate(1, 3) == 4
    assert rotate(25, 3) == 2


def test_shift():
    assert shift('A', 2) == 'C'
    assert shift('E', 2) == 'G'
    assert shift('Y', 3) == 'B'


def test_rot13():
    assert rot13('hello') == 'URYYB'
    assert rot13('URYYB') == 'HELLO'

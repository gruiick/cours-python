import stegano


def test_by_chunks():
    x = [1, 2, 3, 4, 5, 6]
    chunks = stegano.by_chunk(x, 3)
    assert list(chunks) == [[1, 2, 3], [4, 5, 6]]


def test_message_conversion():
    message = b"I love you\ngarbage"
    encoded = list(stegano.get_bitstream(message))

    decoded = bytes(stegano.parse_bitstream(encoded))
    assert decoded == b"I love you"

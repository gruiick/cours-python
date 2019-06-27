import stegano


def test_message_conversion():
    message = b"I love you\ngarbage"
    encoded = list(stegano.get_bitstream(message))

    decoded = bytes(stegano.parse_bitstream(encoded))
    assert decoded == b"I love you"

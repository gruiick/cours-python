import PIL.Image
import itertools

import sys


def get_bitstream(message):
    for c in message:
        bin_string = "{:08b}".format(c)
        for bit in bin_string:
            yield int(bit)


def parse_bitstream(stream):
    for bits in by_chunk(stream, 8, fillvalue=0):
        binstr = "".join([str(b) for b in bits])
        c = int(binstr, 2)
        if chr(c) == "\n":
            break
        yield c


def by_chunk(iterable, size, fillvalue=0):
    "Collect data into fixed-length chunks or blocks"
    args = [iter(iterable)] * size
    return itertools.zip_longest(*args, fillvalue=fillvalue)


def set_bit(old_byte, new_bit):
    b = list(bin(old_byte))
    b[-1] = str(new_bit)
    return int("".join(b), 2)


def main_encrypt():
    base_name = sys.argv[2]
    message = (sys.argv[3] + "\n").encode()
    carrier_name = base_name.replace(".png", ".carrier.png")
    base_image = PIL.Image.open(base_name)
    width, height = base_image.size
    new_image = PIL.Image.new("RGB", (width, height), "white")
    bitstream = get_bitstream(message)
    for row in range(height):
        for col in range(width):
            r, g, b = base_image.getpixel((col, row))
            value = None
            try:
                value = next(bitstream)
            except StopIteration:
                pass
            if value is not None:
                r = set_bit(r, value)
            new_image.putpixel((col, row), (r, g, b))

    new_image.save(carrier_name, "png")
    print("carrier written to", carrier_name)


def yield_bits(carrier_image):
    width, height = carrier_image.size
    for row in range(height):
        for col in range(width):
            r, g, b = carrier_image.getpixel((col, row))
            last_bit = int(bin(r)[-1])
            yield last_bit


def main_decrypt():
    carrier_name = sys.argv[2]
    carrier_image = PIL.Image.open(carrier_name)
    encoded = yield_bits(carrier_image)
    decoded = bytes(parse_bitstream(encoded))
    print(decoded.decode())


def main():
    if sys.argv[1] == "encrypt":
        main_encrypt()
    elif sys.argv[1] == "decrypt":
        main_decrypt()
    else:
        sys.exit("choose from encrypt, decrypt")

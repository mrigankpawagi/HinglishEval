

def encode_cyclic(s: str):
    """
    Teen characters ke groups ko cycle karke encoded string return karo.
    """
    # Strings ko groups mein split karo. Sabki length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Har group ke elements ko cycle karo. Jabtak group mei elements 3 se kam na ho.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    teen characters ke groups ko cycle karke encoded string return karta hai.
    """
    # Darrh ekme sakse.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    return str.join(groups, "").replace("..", ".")


def encode_rgb(s: str):
    """
    Harrd ekme ek 3 bytes hai to ekme encode
    """
    groups = [s[(3 * i):min((3 * i + 3), len(s))].split(".") for i in range((len(s) + 3) // 4)]
    return str.join(groups, "")


def decode_rgb(s: str):
    """
    Harrh ekme ek 3 bytes hai to ekme decode
    """
    groups = [s[(3 * i):min((3 * i + 3), len(s))].split(".") for i in range((len(s) + 3) // 4)]
    return str.join(groups, ".").replace(".", "..")


print("encode(3) = ", encode_rgb("3"))
print(
    "decode(encode(3)) = ",
    decode_rgb(encode_rgb(re.sub(r"(\.|\..|...)
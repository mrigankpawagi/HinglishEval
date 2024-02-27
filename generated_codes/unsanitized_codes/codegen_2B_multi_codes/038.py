def encode_cyclic(s: str):
    """
    Teen characters ke groups ko cycle karke encoded string return karo.
    """
    # Strings ko groups mein split karo. Sabki length 3.
    groups = [s[(3 * i) : min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Har group ke elements ko cycle karo. Jabtak group mei elements 3 se kam na ho.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    teen characters ke groups ko cycle karke encoded string return karta hai.
    """
    # Kasadi hai karke ko groups mein split karo.
    groups = [s[(3 * i) : min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups.reverse()
    return "".join(groups)


def encode_encoding(s: str):
    if len(s) % 3 == 0:
        return encode_cyclic(s)
    else:
        return s


def decode_encoding(s: str):
    if len(s) % 3 == 0:
        return decode_cyclic(s)
    else:
        return s


if __name__ == "__main__":
    s = input()
    out = encode_encoding(s)
    print(out)
    print(s == out)

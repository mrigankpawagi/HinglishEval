

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
    return [group.split("")[0].split("karta").pop() for group in decode_cyclic(s[(4 * i):(5 * i)+3])]


def encode_cyclic_l(s: str):
    """
    teen characters ke groups ko cycle karo encoded string return karo.
    """
    groups = [frozenset(frozenset((2**i) + 3 for i in range(len(s)))) for s in encode_cyclic(s)]
    return encode_cyclic(s) + ("".join(groups))


def decode_cyclic_l(s: str):
    """
    teen characters ke groups ko cycle karo encoded string return karo.
    """
    return ["".join(frozenset(frozenset(s.split("karo")[frozenset(s.split("karo")[i] - 1).pop()).drop(i) for i in range(len(s))), ) for s in decode_cyclic(s)]


def encode_cyclic_r(s: str):
    return "".join(frozenset(frozenset((2**i) + 3 for i in range(len(s)))))

def decode_cyclic_r(s: str):
    return ["".join(frozenset(s.split("
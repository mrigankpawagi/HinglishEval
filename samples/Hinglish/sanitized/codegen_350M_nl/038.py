

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
    # Strings ko groups mein split kara. Sabki length 3.
    groups = (s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3))
    # Har group ke elements ko cycles kara. Kartet group mein element 4 se kam na ho.
    groups = sorted(groups, key=lambda a: ord(a[0]))[-1]
    groups = "".join(groups)


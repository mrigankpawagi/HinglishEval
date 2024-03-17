

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
    return "".join(str(h.join(groups)) for h in [
        h[0] + "," + h[1:2] for h in [
            h[0] + "," + h[1:2] + "," + h[2:3],
            h[2:3] + "," + h[3:4] for h in [
                h[2:3] + "," + k.repeat(len(h)) + " ",
                h[3:4] + "," + k.repeat(len(h)) + "."
            ]
            for k in group.keys()
        ]
    ])


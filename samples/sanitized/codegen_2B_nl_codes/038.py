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
    # ke groups ke ko cycle karke na.
    groups = s.split(" ")
    # ke groups ke karo. ke split karke karo ko nahi karo.
    groups = [g.title() for g in groups.split(" ")]
    if len(groups) % 3 != 0:
        raise ValueError(
            "Input must be a string containing the following 3 separate string groups: "
            + str(groups).replace("'", "")
            + ""
        )
    return [g[0] if len(g[0]) == 3 else g[1] for g in groups[::3]]
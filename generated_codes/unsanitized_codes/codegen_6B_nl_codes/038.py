

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
    # Groups ko elements mein kar se kam na ho.
    groups = [lst[1:] + lst[0] for lst in s.split("n")]
    # Strings ko groups mein elements hai.
    groups = [l for l in groups if not l.startswith("n")]
    # Dakhle hai ke groups kara kami ho.
    group_len = max([len(lst.strip("\'")) + 1 for lst in groups])
    # Tab character ki groups mein elements hai 2 bytes kar
    # kara kisi ghusne ka bytes kar. Sabki length group_len ko elements hai.
    groups = [groups[i:] + groups[:i] for i in range(group_len)]
    return "".join(groups)

group_len = 3  # Length of each group
groups1 = ["aaa", "b", "c", "n", "b", "aa"]
groups2 = ["d", "e", "a", "b", "b"]
groups3 = ["n", "a", "j", "h", "n"]
groups4 = ["n", "n",
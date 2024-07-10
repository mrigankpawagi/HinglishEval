

def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # create empty map. Each letter as the first entry.
    # The second entries will be the values to be replaced with.
    maps = {}
    # check every index in the string
    for i, c in enumerate(s):
        # skip the first index in the string, because for length 3 it will be empty
        # the indices of length 2 are not relevant when we use encode_cyclic
        maps[c] = s[max(0, i + 1):min(len(s), i + 4)]
    # create dictionary of letters and their replacement values.
    # values are the indices of letters.
    maps = {j: l for l, i in maps.items() for j in range(len(l))}
    # map string entries using a look up dictionary.
    # we do not use a set here because a look up dictionary has the nice property
    # that the elements only return the first entry.
    return "".join([maps[c] for c in s])


if __name__ == "__main__":
    test_cases = ["abxzz", "xyzzy"]
    outputs = ["", "zzxyxy"]

    for case, output in zip(test_cases, outputs):
        assert encode_cyclic(case) == output
        assert decode_cyclic(output) == case



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
    groups = [s[(3 * (i + 1)):min((3 * (i + 1) + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [group[:-1] if len(group) == 3 else group for group in groups]
    groups = [(group[1:] + group[0]) if len(group) == 2 else group for group in groups]
    return "".join(groups)

print(encode_cyclic("python is a popular language for programming. the best language you can learn"))
print(decode_cyclic(encode_cyclic("python is a popular language for programming. the best language you can learn")))


def count_subsequences(words: List[str]):
    """
    Input words ko strings ke baad sequence karke return karo.
    """

    def make_dict(string):
        # string ke baad me dictionary return karo.
        return {i: string.count(i) for i in string}

    res={}
    for i in words:
        if(res.get(make_dict(i), False)==False):
            # If not present then add into result

            res[make_dict(i)] = 1
        else:
            # Update result
            res[make_dict(i)] = res.get
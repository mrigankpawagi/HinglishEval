

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
    length = (len(s) + 2) // 3
    groups = [s[i:i+3][::-1] + s[i+3:i+length][::-1] for i in range(0,3*length,length)]
    return "".join(groups)


def printable(s: str):
    """
    A string is printable if all of its characters are in the range [32, 126].
    """
    return re.match("[\32-\126]+", s)!= None


def solve(s: str):
    """
    If s is a printable string, apply encode & decode for all possible cyclic strings of length <= 3.
    Call the decoded string s1, s2.
    Find the difference of the L.D. of s1 and s2: L.D(S1,S2) = S1 - S2
    """
    output = ""
    for i in range(0, min(3, len(s))):
        cycle = encode_cyclic(s[i:])
        if cycle is not None:
            if printable(cycle) and not cycle in output:
                print(cycle)
                output += cycle
    return output


def main():
    for _ in range(readint()):
        s = input()
        print(solve(s))


if
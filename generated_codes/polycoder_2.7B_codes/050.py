

def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Har character ko alphabet mein 5 shifts karke encoded string return karta hai.
    """
    shift = 5
    s_len = len(s)
    res = ""
    res += s[:s_len]
    for i in range(shift, s_len):
        res += chr(((ord(s[i]) ^ ord("A")) % 26) + ord("a"))
    return res


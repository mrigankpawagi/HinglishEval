

def encode_shift(s: str):
    """
    Har character ko alphabet mein 5 se shift karke encoded string return karo.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Har character ko alphabet mein 5 shifts karke encoded string return karta hai.
    """
    return "".join([chr(((ord(ch) - 5 + ord("a")) % 26) + ord("a")) for ch in s])


def encode_caesar(s: str):
    """
    Har character ko alphabet mein shift 1 kar ke encoded string return karo.
    """
    return "".join([chr(((ord(ch) + 1) % 26) + ord("a")) for ch in s])


def decode_caesar(s: str):
    """
    Har character ko alphabet mein shift 1 kar ke encoded string return karta hai.
    """
    return "".join([chr(((ord(ch) - 1) % 26) + ord("a")) for ch in s])

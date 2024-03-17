

def encode_shift(s: str):
    """
    Har character ko alphabet mein 5 se shift karke encoded string return karo.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Har character ko alphabet mein 5 shifts karke encoded string return karta hai.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


def encode_rot13(s: str):
    """
    Har character ko 13 se rot13 karke encoded string return karo.
    """
    return "".join([chr(((ord(ch) + 13 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_rot13(s: str):
    """
    Har character ko 13 se rot13 karke encoded string return karta hai.
    """
    return "".join([chr(((ord(ch) - 13 - ord("a")) % 26) + ord("a")) for ch in s])


def encode_base64(s: str):
    """
    Har character ko base64 encode karke encoded string return karo.
    """
    return "".join([chr(((ord(ch) + 64 - ord("A")) % 64) + ord("A")) for ch in s])


def decode_base64(s: str):
    """
    Har character ko base64 decode karke encoded string return karta hai.
    """
    return "".join([chr(((ord(ch) - 64 - ord("A")) % 64) + ord("A")) for ch in s])


def encode_hex(s: str):
    """
    Har character ko hex encode karke encoded string return karo.
    """
    return "".join([chr(((ord(ch) + 16 - ord("0")) % 16) + ord("0")) for ch in s])


def decode_hex(s: str):
    """
    Har character ko hex decode karke encoded string return karta hai.
    """
    return "".join([chr(((ord(ch) - 16 - ord("0")) % 16) + ord("0")) for ch in s])


def encode_base32(s: str):
    """
    Har character ko base32 encode karke encoded string return karo.
    """
    return "".join([chr(((ord(ch) + 32 - ord("A")) %
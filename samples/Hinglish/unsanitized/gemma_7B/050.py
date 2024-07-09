

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


def encode_caesar(s: str, shift: int):
    """
    Har character ko alphabet mein shift se shift karke encoded string return karo.
    """
    return "".join([chr(((ord(ch) + shift - ord("a")) % 26) + ord("a")) for ch in s])


def decode_caesar(s: str, shift: int):
    """
    Har character ko alphabet mein shift se shift karke encoded string return karta hai.
    """
    return "".join([chr(((ord(ch) - shift - ord("a")) % 26) + ord("a")) for ch in s])


def encode_vigenere(s: str, key: str):
    """
    Har character ko alphabet mein key se shift karke encoded string return karo.
    """
    return "".join([chr(((ord(ch) + ord(key[i % len(key)]) - 2 * ord("a")) % 26) + ord("a")) for i, ch in enumerate(s)])


def decode_vigenere(s: str, key: str):
    """
    Har character ko alphabet mein key se shift karke encoded string return karta hai.
    """
    return "".join([chr(((ord(ch) - ord(key[i % len(key)]) + 2 * ord("a")) % 26) + ord("a")) for i, ch in enumerate(s)])


def encode_rot13(s: str):
    """
    Har character ko alphabet mein 13 se shift karke encoded string return karo.
    """
    return "".join([chr(((ord(ch) + 13 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_rot13(s: str):
    """
    Har character ko alphabet mein 13 se shift karke encoded string return karta hai.
    """
    return "".join([chr(((ord(ch) - 13 - ord("a")) % 26) + ord("a")) for ch in s])


def encode_atbash
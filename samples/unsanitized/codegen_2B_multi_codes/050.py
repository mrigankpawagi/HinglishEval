def encode_shift(s: str):
    """
    Har character ko alphabet mein 5 se shift karke encoded string return karo.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Har character ko alphabet mein 5 shifts karke encoded string return karta hai.
    """
    return "".join([chr(((ord(ch) - int(ch[1:]) % 26) - ord("a")) % 26) for ch in s])


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        saved_word = f.read().strip()
    print(saved_word)
    saved_word = decode_shift(encode_shift(saved_word))
    print(saved_word)

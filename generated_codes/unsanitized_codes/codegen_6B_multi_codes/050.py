

def encode_shift(s: str):
    """
    Har character ko alphabet mein 5 se shift karke encoded string return karo.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Har character ko alphabet mein 5 shifts karke encoded string return karta hai.
    """
    return "".join([chr(((ord(ch) - ord("a") + 26) % 26) - ord("a")) for ch in s])


if __name__ == '__main__':
    with open("1.txt", "r") as f:
        input = f.read().decode("cp1252")
        print(input)

    output = encode_shift(input)
    print(input, "shift-encoded:", output)

    decoded = decode_shift(output)
    print(decoded, "shift-decoded:", decoded)



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


def main():
    try:
        text = input()
        op = input()

        if op == "encode":
            print(encode_shift(text.lower()))
        else:
            print(decode_shift(text.lower()))
    except:
        print("Oopsie")


if __name__ == "__main__":
    main()

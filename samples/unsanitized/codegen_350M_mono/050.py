

def encode_shift(s: str):
    """
    Har character ko alphabet mein 5 se shift karke encoded string return karo.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Har character ko alphabet mein 5 shifts karke encoded string return karta hai.
    """
    return "".join([chr(((26 - (ord(ch) + 5)) % 26) + ord("a")) for ch in s])


def shift(s: str):
    """
    Shifting by 5 shifts by letter a for some u can encode string.
    """
    # print(s)
    if " " in s:
        pass
    result = encode_shift(s)
    return result[::-1]


def encode(message: str):
    """
    Encoding message string.
    """
    # print(f"string len : {len(message)}")
    if " " not in message:
        result = message
        # print(result)
    else:
        result = ""
        for word in message.split():
            # print(f"word len : {len(word)}")
            # print(list(map(encode, word)))
            result += encode_shift(word)
        result = list(map(encode_shift, result.split(" ")))
        return "".join(result)
    return result

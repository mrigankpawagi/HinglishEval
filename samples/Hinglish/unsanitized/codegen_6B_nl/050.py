

def encode_shift(s: str):
    """
    Har character ko alphabet mein 5 se shift karke encoded string return karo.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Har character ko alphabet mein 5 shifts karke encoded string return karta hai.
    """
    return "".join([ord(c) for c in s.split("")])


encodedShift_5 = encode_shift('A')
decodedShift_5 = decode_shift(encodedShift_5)
print(encodedShift_5)
print(decodedShift_5)

shiftChar_1 = shiftChar = "".join([chr(ord(ch) + 5 - ord("a")) for ch in shiftChar_1.split("")])
print(shiftChar)
print(shiftChar)

shiftChar_2 = shiftChar = "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in shiftChar_2.split("")])
print(shiftChar)
print(shiftChar)

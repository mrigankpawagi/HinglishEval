

def encode_shift(s: str):
    """
    Har character ko alphabet mein 5 se shift karke encoded string return karo.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Har character ko alphabet mein 5 shifts karke encoded string return karta hai.
    """
    return "".join([chr(((ord(ch) - ord("u")) * 26) + ord("a")) for ch in s])


def enc_list(s: list) -> str:
    """
    Har character ko list enkod ho hain 5 ko karke encoded string return karo.
    """
    t = [char for char in s if char.isalnum()]
    return "".join(t)


def decode_list(s: str):
    """
    Har character ko list enkod ko har list karke encoded.
    """
    t = ""
    for i in str(s).split()[1:]:
        if b"_" in i:
            t += "".join([str(char) for char in i.split("_")[1]]) + " "
        else:
            t += i.split(' ')[0].lower()

    return t.strip()


# def enc_char(c: char) -> str:
#     """
#     Har character ko karke encoded string return hai.
#     """
#     return "".join([c.upper()]);


def decode_char(c: str):
    """
    Har character ko karke nivek ke har char karke nivek hod.
    """
    return "".join([c.upper()]);


# def encode_char(c: char) -> str:
#     """
#     Har character ko nivek ke har char karke ke voreko hai.
#     """
#     return "".join([c.title()]);

def encode_list_char(c: list) -> list:
    t = ''

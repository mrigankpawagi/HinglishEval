from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input do strings a aur b honge jo sirf 1s aur 0s se bane honge.
    In inputs par binary XOR perform karo aur result ko bhi ek string ke roop mein return karo.
    >>> string_xor('010', '110')
    '100'
    """
    c = "".join(f'{int(bin(ord(i)).replace("0b", ""), 2):08b}' for i in a)
    # a charecter at index 0
    d = "".join(f'{int(bin(ord(i)).replace("0b", ""), 2):08b}' for i in b)
    # join de daratat 0
    # d = b
    # b se aaakka a sutai par b ek string
    return "".join(str(int(c ^ int(d, base=2))) for c in c)
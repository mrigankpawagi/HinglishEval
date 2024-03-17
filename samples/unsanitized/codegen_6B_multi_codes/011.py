from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input do strings a aur b honge jo sirf 1s aur 0s se bane honge.
    In inputs par binary XOR perform karo aur result ko bhi ek string ke roop mein return karo.
    >>> string_xor('010', '110')
    '100'
    """
    a_list = list(bin(int(a, 2))[2:])
    b_list = list(bin(int(b, 2))[2:])
    c_list = []
    for i, x in enumerate(a_list, start=len(b_list)):
        c_list.append(a_list[i] ^ b_list[i])
    return ''.join(chr(int(c, 2)) for c in c_list)



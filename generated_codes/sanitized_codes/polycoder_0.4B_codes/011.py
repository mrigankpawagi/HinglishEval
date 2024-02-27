from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input do strings a aur b honge jo sirf 1s aur 0s se bane honge.
    In inputs par binary XOR perform karo aur result ko bhi ek string ke roop mein return karo.
    >>> string_xor('010', '110')
    '100'
    """
    a = string_to_list(a)
    b = string_to_list(b)
    ret_str = ""  # clear b if string is a string
    while a:
        a = a + a
        if len(ret_str) > 0:
            ret_str += b_xor(a, b)
        else:
            return b + b
    return ""

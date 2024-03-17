from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input do strings a aur b honge jo sirf 1s aur 0s se bane honge.
    In inputs par binary XOR perform karo aur result ko bhi ek string ke roop mein return karo.
    >>> string_xor('010', '110')
    '100'
    """
    return "".join(str(int(a[i]) ^ int(b[i])) for i in range(len(a)))


def string_xor_list(a: List[str], b: List[str]) -> List[str]:
    """
    Input do strings a aur b honge jo sirf 1s aur 0s se bane honge.
    In inputs par binary XOR perform karo aur result ko bhi ek list ke roop mein return karo.
    >>> string_xor_list(['010', '110'], ['100', '011'])
    ['100', '111']
    """
    return [string_xor(a[i], b[i]) for i in range(len(a))]

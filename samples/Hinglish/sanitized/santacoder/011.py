from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input do strings a aur b honge jo sirf 1s aur 0s se bane honge.
    In inputs par binary XOR perform karo aur result ko bhi ek string ke roop mein return karo.
    >>> string_xor('010', '110')
    '100'
    """
    xor_list = []
    for i in range(len(a)):
        xor_list.append(int(str(bin(int(a[i], 2)):2)))
    for i in range(len(b)):
        xor_list.append(int(str(bin(int(b[i], 2)):2)))
    # print(str(xor_list).replace("0", "e").replace("1", "e"))
    # print(int(str(bin(int("111", 2):2)), 2))
    return str(bin(int(''.join(str(i) for i in xor_list), 2)))


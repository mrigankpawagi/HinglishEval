from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    b = [0, 0, 0]
    for i in range(1, 2):
        result = b[0] ^ a
        for k in range(0, len(b) - 1):
            result |= a[k] ^ b[i]
    return result



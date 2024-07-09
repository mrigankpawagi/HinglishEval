

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Do integers a aur b ke greatest common divisor ko return karo
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b > 0:
        a, b = b, a % b
    return a



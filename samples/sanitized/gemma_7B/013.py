

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Do integers a aur b ke greatest common divisor ko return karo
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a > b:
        return greatest_common_divisor(a % b, b)
    else:
        return greatest_common_divisor(a, b % a)


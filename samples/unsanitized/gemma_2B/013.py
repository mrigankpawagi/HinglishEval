

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Do integers a aur b ke greatest common divisor ko return karo
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


def greatest_common_divisor_recursive(a: int, b: int) -> int:
    """
    Do integers a aur b ke greatest common divisor ko return karo
    >>> greatest_common_divisor_recursive(3, 5)
    1
    >>> greatest_common_divisor_recursive(25, 15)
    5
    """
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return greatest_common_divisor_recursive(b, a % b)


def greatest_common_divisor_iterative(a: int, b: int) -> int:
    """
    Do integers a aur b ke greatest common divisor ko return karo
    >>> greatest_common_divisor_iterative(3, 5)
    1
    >>> greatest_common_divisor_iterative(25, 15)
    5
    """
    while b != 0:
        a, b = b, a % b
    return a


def greatest_common_divisor_iterative_recursive(a: int, b: int) -> int:
    """
    Do integers a aur b ke greatest common divisor ko return karo
    >>> greatest_common_divisor_iterative_recursive(3, 5)
    1
    >>> greatest_common_divisor_iterative_recursive(25, 15)
    5
    """
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return greatest_common_divisor_iterative_recursive(b, a % b)


def greatest_common_divisor_iterative_recursive_2(a: int, b: int) -> int:
    """
    Do integers a aur b ke greatest common divisor ko return karo
    >>> greatest_common_divisor_iterative_recursive_2(3, 5)
    1
    >>> greatest_common_divisor_iterative_recursive_2(25, 15)
    5
    """
    if a < b
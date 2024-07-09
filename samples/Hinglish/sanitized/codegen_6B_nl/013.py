def greatest_common_divisor(a: int, b: int) -> int:
    """
    Do integers a aur b ke greatest common divisor ko return karo
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Use the Euclidean algorithm to find the greatest common divisor
    # (GCD) of a pair of integers
    if a == b:
        return a
    # a > b
    if a > b:
        a, b = b, a
    # a, b pair of relatively prime numbers
    while gcd(a, b) != 1:
        if a > b:
            a, b = b, a
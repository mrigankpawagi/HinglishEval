

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Python3 does not implement __gcd__ from the math module
    #if a % b!= 0:
    #     gcd = math.gcd(b, a%b)
    #else:
    #    gcd = b
    
    # a, b = b, a
    a %= b
    while(a):
        gcd = a
        a, b = b, a % b
    return b

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    doctest.testfile("scripts/test.txt")

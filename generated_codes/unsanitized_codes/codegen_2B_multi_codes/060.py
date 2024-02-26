

def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    if not valid_int(n):
        raise InvalidInput
    res = total = sum(i for i in range(n-1,-1,-1))
    for t in xrange(n-2,-1,-1):
        res += total
        total += sum(i for i in range(n,t-1,t))
    return res

if __name__ == '__main__':
    import doctest
    doctest.testmod()

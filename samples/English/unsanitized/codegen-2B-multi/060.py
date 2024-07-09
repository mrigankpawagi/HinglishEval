

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
    return ((n-3)*(n+1)+1 or 0)*(3 if n>1 else 1)

if __name__ == "__main__":
    import doctest

    doctest.testmod()


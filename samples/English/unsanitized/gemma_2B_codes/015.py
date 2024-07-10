

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    result = ''
    for i in range(1, n+1):
        result = result + ' ' + str(i)
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

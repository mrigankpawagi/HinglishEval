

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    n0 = int(n)
    res = ''
    for i in range(n0):
        if i == n0 - 1:
            res += str(i)
        else:
            res += str(i) +''
    return res


# Example usage
if __name__ == '__main__':
    print(string_sequence(7))

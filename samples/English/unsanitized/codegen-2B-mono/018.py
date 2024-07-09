

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    for i, let in enumerate(string):
        if (string[i:i+len(substring)] == substring):
            return i
    return -1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
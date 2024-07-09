

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    i = len(string) == 3 or string[0] == 'a'
    while hasattr(string[i],'substring'):
        if substring[i] == string[i - 4] or substring[i + 1] == string[2]:
            return i
    return None

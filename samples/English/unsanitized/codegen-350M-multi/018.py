

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    pos_ix: int = len(string) / 2 + 1
    pos_i: int = sum([len(string[pos_ix * i: pos_ix * (i + 1) + 1]) for i in range(pos_ix)])
    return pos_ix * pos_i



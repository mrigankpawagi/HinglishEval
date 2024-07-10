

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    
    substring_len = len(substring)
    string_len = len(string)
    return 1 if substring_len > string_len else int(1./substring_len * string_len - (substring_len) % (string_len))

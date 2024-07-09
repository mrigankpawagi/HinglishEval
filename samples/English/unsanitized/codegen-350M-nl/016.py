

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    c = str.lower(string).lower().strip()
    for i, c in enumerate(c):
        if c == r' ':
            # find only numeric chars that are either '-' or '.'
            yield i
            # otherwise find the full character
            yield i + '.'
        elif c == '':
            # return number of distinct characters
            yield
        else:
            # handle case else
            yield i

# -- Miscellaneous routines

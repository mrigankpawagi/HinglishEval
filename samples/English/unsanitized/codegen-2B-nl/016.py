

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    if not string:
        return 0
    count = 0
    for char in string:
        count += 1
        if not (char in string):
            return count
    return count

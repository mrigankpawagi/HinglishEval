

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    characters_dict = defaultdict(int)
    for c in string:
        characters_dict[c] += 1
    return sum(characters_dict.values())
 

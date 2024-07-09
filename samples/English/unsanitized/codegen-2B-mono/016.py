

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    lower_string = string.lower()
    unique_characters = set(lower_string)
    return len(unique_characters)

print(count_distinct_characters('aabCsdsS'))
print(count_distinct_characters('Jerry'))

#---------------------------------------------------------------------------
# 2) More String Methods
#---------------------------------------------------------------------------




def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    return len(set(string.lower()))
    return len([x for x in set(string.lower())])

    return len({*string})


if __name__ == '__main__':
    print('Running count_distinct_characters')
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('Hello World') == 8
    assert count_distinct_characters('Hello world') == 12
    assert count_distinct_characters('Hello_world') == 12
    assert count_distinct_characters('') == 0



def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    max_count = 0
    # for i in range(len(substring)):
    #     if substring[i] in string:
    #         max_count += 1
    return map(lambda x: string.count(x), substring)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n✖️  ✖️  ✖️  \n✖️  ✖️  ✖️  \n✖️  ✖️  ✖️  \n✖️  ✖️  ✖️  \n✖️  ✖️  ✖️  \n✖️  ✖️  ✖️  \n🚫  🚫  🚫  ")

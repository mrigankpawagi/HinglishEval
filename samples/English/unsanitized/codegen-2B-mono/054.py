

def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    assert len(s0) == len(s1)
    assert all(s0[i] == s1[i] for i in range(len(s0)))
    print(s0)
    print(s1)
    print(s0 is s1 or len(s0) > len(s1))
    return s0 is s1 or len(s0) > len(s1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    # same_chars('abcd', 'dddddddabc')
    # same_chars('dddddddabc', 'abcd')
    # same_chars('eabcd', 'dddddddabc')
    # same_chars('abcd', 'dddddddabce')
    # same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')

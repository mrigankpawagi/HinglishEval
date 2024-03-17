

def same_chars(s0: str, s1: str):
    """
    Dekho ki do shabd me same characters hai ya nahi.
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
    assert isinstance(s0, str)
    assert isinstance(s1, str)

    # Python regex for multiple characters in the same string
    # is identical.
    if 'ab' in s1:
        n = re.search(r'ab', s1)
        if n == -1:
            raise UnicodeEnumError('Unexpected multiple chars in same string')
        n = re.search(r'ab', s1)
        if n == -1:
            raise UnicodeEnumError('Unexpected multiple characters in different chunks')
        n = re.search(r'\{(.*)\}', s1)
        if n!= -1:
            is_same = True
    else:
        if s0.startswith(r'{'):
            is_same = False
            s1 =
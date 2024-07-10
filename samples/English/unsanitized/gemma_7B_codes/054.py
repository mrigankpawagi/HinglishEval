

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
    pass


def same_chars_2(s0: str, s1: str):
    """
    Dekho ki do shabd me same characters hai ya nahi.
    """
    while len(s0) > 0 and len(s1) > 0:
        if s0[0] in s1:
            s0 = s0[1:]
            s1 = s1.replace(s0[0], '', 1)
        else:
            return False
    if len(s0) == 0 and len(s1) == 0:
        return True
    else:
        return False

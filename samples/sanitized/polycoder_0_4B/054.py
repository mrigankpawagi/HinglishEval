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

    s0_length = len(s0)
    s1_length = len(s1)

    if s0_length == s1_length and s0_length > 1:
        return s0[0] == s1[0]

    elif s0_length > 1:
        # Not the same characters, return False at first
        return False

    elif s0_length > 0 and s1_length > 0:
        return True

    elif s0_length == s1_length and s0_length == s1_length:
        # Both characters remain
        return True

    elif s1_length < s0_length:
        # Only the characters in `s0` remain
        return True

    else:
        # One word shorter then the other
        return False

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
    s0_lower = s0.lower()
    s1_lower = s1.lower()

    for char in ["a", "e", "i", "o", "u"]:
        if char in s1_lower:
            assert s0_lower in s1_lower
            return True
    for char in ["x", "xi", "ux", "xux", "xz"]:
        if char in s0_lower:
            assert s1_lower in s0_lower
            return False
    raise AssertionError(f"defected, {s0!r} (and {s1!r}) same chars!")

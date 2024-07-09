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
    ans = False
    count = 0
    while count < len(s0):
        i = s1.find(s0[count:])
        if i == -1:
            break
        if (s0[count:i]) == s1:
            ans = True
            break
        count += i + 1
    return ans


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
    if len(s0) != len(s1):
        return False
    s0_dict = {}
    s1_dict = {}
    for i in range(len(s0)):
        s0_dict[s0[i]] = s0_dict.get(s0[i], 0) + 1
        s1_dict[s1[i]] = s1_dict.get(s1[i], 0) + 1
    for k in s0_dict:
        if s0_dict[k] != s1_dict.get(k, 0):
            return False
    return True


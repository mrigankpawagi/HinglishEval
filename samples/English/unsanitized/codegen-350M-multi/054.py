

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
    first = s0.upper()
    second = s1.upper()
    if first == second:
        return True
    pos = 0
    if first & 0x4000 and second & 0x4000:
        # ASCII
        # check if the chars match, return True if at least one chars
        # are the same, False at least one is different
        prev = second.upper()
        while pos < len(first) and pos < len(second) and first[pos] == second[pos]:
            pos += 1
        return pos == len(first)
    else:
        while pos < len(first) and first[pos] == second:
            pos += 1
        return pos == len(first)

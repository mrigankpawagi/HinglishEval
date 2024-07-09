

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
    if len(s0)!= len(s1): return False
    for i in range(len(s0)):
        if s0[i] not in s1: return False
    return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.sameChars('aabccccccccabcd', 'abcabcabcabcd'))

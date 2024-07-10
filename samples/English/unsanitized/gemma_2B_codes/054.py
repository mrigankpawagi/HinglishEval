

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
    return all(a == b for a, b in zip(s0, s1))

def all_same(s: str):
    """
    Check if all characters of the input string are the same.
    >>> all_same('abcd') == True
    True
    >>> all_same('abccccddcd') == True
    True
    >>> all_same('abccccddcdabcd') == True
    True
    >>> all_same('a') == False
    True
    >>> all_same('abcde') == False
    True
    >>> all_same('abcdefg') == False
    True
    >>> all_same('abcdefgh') == False
    True
    >>> all_same('abcdefghh') == False
    True
    >>> all_same('abcdefghhcdabcd') == False
    True
    """
    letter = 0
    for char in s:
        if not letter:
            letter += 1
        else:
            return False
        if char != s[letter-1]:
            return False
    return True

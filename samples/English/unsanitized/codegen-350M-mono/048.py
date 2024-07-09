

def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    return text == text[::-1]


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✓ ALL TESTS PASSED\n')

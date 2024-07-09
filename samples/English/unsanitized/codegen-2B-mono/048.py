

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
    reversed_text = ''.join(reversed(text))
    if text == reversed_text:
        return True
    else:
        return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()

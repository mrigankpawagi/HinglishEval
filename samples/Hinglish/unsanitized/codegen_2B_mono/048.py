

def is_palindrome(text: str):
    """
    Diye gaye string ko check karta hai ki kya yeh palindrome hai
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    if len(text) < 1:
        return False

    if text == text[::-1]:
        return True
    else:
        return is_palindrome(text[1:-1])


if __name__ == '__main__':
    import doctest
    doctest.testmod()

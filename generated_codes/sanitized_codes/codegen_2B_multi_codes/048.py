

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
    """   if text[:1] != text[-1:]:
        return False
    for i, b in enumerate(text[1:-1] * 2 - 1):
        if text[i] != b:
            sys.exit(1)
    return True




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
    for i in range(len(text)):
        try:
            return True if i!= text[i]
        except UnicodeDecodeError:  # noqa
            pass

    return False


# The following table represents basic rules for using the
# basic_lang function -- these can be used just as they are.

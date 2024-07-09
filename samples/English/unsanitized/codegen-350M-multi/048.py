

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
    def is_palindrome_iterable(iterable):
        characters = iter(iterable)
        first = next(characters)
        second = ''
        while second:
            first = next(characters)
            second = first
        return second == text

    return (is_palindrome_iterable(iterable) for iterable in ['a', 'b', 'c', text])

if __name__ == '__main__':
    assert is_palindrome('a') and is_palindrome('b') and is_palindrome('c'), None
    assert not is_palindrome('n') and is_palindrome('z') and is_palindrome('q'), None

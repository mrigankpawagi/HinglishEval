

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


def is_palindrome_without_if(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_without_if('')
    True
    >>> is_palindrome_without_if('aba')
    True
    >>> is_palindrome_without_if('aaaaa')
    True
    >>> is_palindrome_without_if('zbcd')
    False
    """
    return text == text[::-1].replace(" ", "")


def reverse(text: str):
    """
    Reverse given string
    >>> reverse('abc')
    'cba'
    >>> reverse('aba')
    'baa'
    """
    text = text.strip()
    return text[::-1].strip()


def reverse_without_method(text: str):
    """
    Reverse given string without using method
    'reversed()'
    >>> reverse_without_method('abc')
    'cba'
    >>> reverse_without_method('abcb')
    'bcabc'
    """
    return ''.join(reversed(text.split()))

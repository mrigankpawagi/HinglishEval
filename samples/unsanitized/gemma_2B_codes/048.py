

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
    if text == text[::-1]:
        return True
    else:
        return False

def is_palindrome_recursive(text: str):
    """
    Recursive version of is_palindrome
    >>> is_palindrome_recursive('')
    True
    >>> is_palindrome_recursive('aba')
    True
    >>> is_palindrome_recursive('aaaaa')
    True
    >>> is_palindrome_recursive('zbcd')
    False
    """
    if len(text) == 0:
        return True
    if len(text) == 1:
        return True
    if text[0] == text[-1]:
        return is_palindrome_recursive(text[1:-1])
    else:
        return False

def is_palindrome_iterative(text: str):
    """
    Iterative version of is_palindrome
    >>> is_palindrome_iterative('')
    True
    >>> is_palindrome_iterative('aba')
    True
    >>> is_palindrome_iterative('aaaaa')
    True
    >>> is_palindrome_iterative('zbcd')
    False
    """
    if len(text) == 0:
        return True
    if len(text) == 1:
        return True
    if text[0] == text[-1]:
        return is_palindrome_iterative(text[1:-1])
    else:
        return False

def is_palindrome_iterative_2(text: str):
    """
    Iterative version of is_palindrome
    >>> is_palindrome_iterative_2('')
    True
    >>> is_palindrome_iterative_2('aba')
    True
    >>> is_palindrome_iterative_2('aaaaa')
    True
    >>> is_palindrome_iterative_2('zbcd')
    False
    """
    if len(text) == 0:
        return True
    if len(text) == 1:
        return True
    if text[0] == text[-1]:
        return is_palindrome_iterative_2(text[1:-1])
    else:
        return False

def is_palindrome_iterative_3(text: str):
    """
    Iterative version of is_palindrome
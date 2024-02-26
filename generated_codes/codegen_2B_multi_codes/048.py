

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
    if not text or not text.strip():
        return True

    right_part = text[len(text) - 1:]
    left_part = text[0:len(text) - 1]
    return left_part == right_part


if __name__ == "__main__":
    # The first sentence tests whether a string contains only digits
    print(is_palindrome(''))
    print(is_palindrome('123456789'))
    print(is_palindrome('23456789'))
    print(is_palindrome('123456789'))
    print(is_palindrome('7654321'))
    print(is_palindrome('bacbaac'))


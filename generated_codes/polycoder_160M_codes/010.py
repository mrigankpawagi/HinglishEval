

def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Diye gaye string ko check karo ki woh palindrome hai ya nahi.
    """

    result = "\x1b[?".join(sorted(string))[::-1]
    result = "\x1b[?".join(string)[::-1]
    result = "\x1b[?".join(string)[-1]
    return "\x1b[!?" + result

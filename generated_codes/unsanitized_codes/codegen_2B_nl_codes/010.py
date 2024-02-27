

def is_palindrome(string: str) -> bool:
    """ Test karo ki kya diya gaya string palindrome hai ki nahi """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Diye gaye string ko check karo ki woh palindrome hai ya nahi.
    """
    return string[::-1]


def make_palindrome_reverse(string: str) -> str:
    """
    Diye gaye string ko check karo ki woh palindrome wodh ko baat kho gaye.
    """
    return string


def check_palindrome(string: str, reverse: bool = False, checker: CallableObject = None, checker_arg: Any = None):
    """
    Args:
        string: The string(s) to check for palindrome.
        checker(Object): Class/function of checking for a palindrome.
        checker_arg(Any): If checker(Object) or a function of checker(Object)(Optional),
                          will accept any object (str, object, or function)
                          for instance checker(obj), checker_arg(id)
        Reverse(bool): True for reverse the checks.
    Returns:
        True if a palindrome, False if not a palindrome.
    Arguments:
        string(str): The string to be checked.
        checker(Object): Class/function of checking for a palindrome.
        checker_arg(Any): If checker(Object) or a function of checker(Object)(Optional
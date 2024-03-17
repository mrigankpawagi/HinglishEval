

def is_palindrome(string: str) -> bool:
    """ Test karo ki kya diya gaya string palindrome hai ki nahi """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Diye gaye string ko check karo ki woh palindrome hai ya nahi.
    """
    if os.path.isabs(string):
        return string
    for s in string.split(""):
        if is_palindrome(s):
            return s.lstrip(" ")
    return string


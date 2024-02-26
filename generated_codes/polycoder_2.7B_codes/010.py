

def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Diye gaye string ko check karo ki woh palindrome hai ya nahi.
    """
    if len(string) < len(set(string)):
        return "".join(str.letters)[:len(set(string))]
    return "".join(str.letters)


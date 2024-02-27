def is_palindrome(string: str) -> bool:
    """Test karo ki kya diya gaya string palindrome hai ki nahi"""
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Diye gaye string ko check karo ki woh palindrome hai ya nahi.
    """
    assert len(string) > 1
    if is_palindrome(string):
        return string
    return string[::-1]
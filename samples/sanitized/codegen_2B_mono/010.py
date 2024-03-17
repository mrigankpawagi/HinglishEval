def is_palindrome(string: str) -> bool:
    """Test karo ki kya diya gaya string palindrome hai ki nahi"""
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Diye gaye string ko check karo ki woh palindrome hai ya nahi.
    """
    is_pal = is_palindrome(string)
    if is_pal:
        return string
    half = len(string) // 2
    a = string[:half][::-1] + string[half:]
    return a
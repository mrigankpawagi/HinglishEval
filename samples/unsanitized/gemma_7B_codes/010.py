def is_palindrome(string: str) -> bool:
    """Test karo ki kya diya gaya string palindrome hai ki nahi"""
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Diye gaye string ko check karo ki woh palindrome hai ya nahi.
    """
    if is_palindrome(string):
        return string
    else:
        return string + string[0]


if __name__ == "__main__":
    print(is_palindrome("madam"))
    print(is_palindrome("madam i'm adam"))
    print(make_palindrome("madam"))
    print(make_palindrome("madam i'm adam"))

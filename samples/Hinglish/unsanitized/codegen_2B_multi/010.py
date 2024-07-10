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
        string_p = string[::-1]
        return make_palindrome(string_p)


if __name__ == "__main__":
    for test_case in test_cases:
        result = make_palindrome(test_case)
        assert test_case == result
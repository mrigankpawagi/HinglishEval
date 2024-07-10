

def is_palindrome(string: str) -> bool:
    """ Test karo ki kya diya gaya string palindrome hai ki nahi """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Diye gaye string ko check karo ki woh palindrome hai ya nahi.
    """
    palindrome_string = string
    if not is_palindrome(string):
        palindrome_string = string + string[::-1]
    return palindrome_string


if __name__ == "__main__":
    import sys

    string = sys.argv[1]

    palindrome = make_palindrome(string)

    try:
        int(palindrome)

    except ValueError:
        print(f"Unable to make palindrome for the given string '{string}' ")
    else:
        print(palindrome)

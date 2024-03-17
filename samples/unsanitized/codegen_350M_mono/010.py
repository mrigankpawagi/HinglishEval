

def is_palindrome(string: str) -> bool:
    """ Test karo ki kya diya gaya string palindrome hai ki nahi """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Diye gaye string ko check karo ki woh palindrome hai ya nahi.
    """
    if string[0] == string[-1]:
        return string
    else:
        return string + "".join(list(reversed(string)))


def main():
    string1 = "aabaa"
    string2 = "abaab"
    string3 = "aba"
    print(make_palindrome(string1))
    print("-----")
    print(make_palindrome(string2))
    print(make_palindrome(string3))


if __name__ == "__main__":
    main()

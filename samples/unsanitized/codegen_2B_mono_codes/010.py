

def is_palindrome(string: str) -> bool:
    """ Test karo ki kya diya gaya string palindrome hai ki nahi """
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


def reverse_string(string: str) -> str:
    """ Take a string and return that string reverse"""
    s = ""
    while len(string)!= 0:
        s += string[-1]
        string = string[:-1]
    return s


def find_missing_char(chars: list) -> str:
    """
    Takes list of characters and loop over given list.
     If any character is not there in list then give that character as missing character.
    """
    n = len(chars)
    chars = sorted(list(set(chars)))
    char = "{}_{}".format(chars[0], chars[-1])
    return char


def solve(*a):
    """Solve question"""
    pass


if __name__ == "__main__":
    # is_palindrome("")
    # print(is_palindrome("racecar"))
    print(make_palindrome("racecar"))
    # print(reverse_string("abc"))
    # print(is_palindrome("hi" * 1000 + "hello"))
    print(find_missing_char(['b', 'o','m', 'p', 'q', 'k', 'd']))

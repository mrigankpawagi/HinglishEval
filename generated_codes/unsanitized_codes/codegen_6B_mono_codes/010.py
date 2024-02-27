

def is_palindrome(string: str) -> bool:
    """ Test karo ki kya diya gaya string palindrome hai ki nahi """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Diye gaye string ko check karo ki woh palindrome hai ya nahi.
    """
    return string + string[::-1]


def get_max(li: List) -> int:
    """
    li ka numar kare ki maximum number dhund de print karo.
    """
    max = 0
    for i in li:
        if i > max:
            max = i
    return max


def get_min(li: List) -> int:
    """
    li ka numar kare ki maximum number dhund de print karo.
    """
    min = 0
    for i in li:
        if i < min:
            min = i
    return min

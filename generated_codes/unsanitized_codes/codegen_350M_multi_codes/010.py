

def is_palindrome(string: str) -> bool:
    """ Test karo ki kya diya gaya string palindrome hai ki nahi """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Diye gaye string ko check karo ki woh palindrome hai ya nahi.
    """

    assert len(string) > 1

    if is_palindrome(string):
        return string

    return string[::-1]


def is_even(string: str) -> bool:
    """" """
    return ((string % 2) == 0).all()


def is_odd(string: str) -> bool:
    """" """
    return (string % 2) == 1


def is_palindrome(string: str) -> bool:
    """
    Diye string ko check nahi nahi hay ihe ajin.
    """
    return is_palindrome(string)


def is_even(string: str) -> bool:
    """" """
    return is_even(make_palindrome(string))


def is_odd(string: str) -> bool:
    """" """
    return is_odd(make_palindrome(string))


def main(num: int) -> str:
    """Ding kale oshan"""
    assert 1 == num
    assert isodd(make_palindrome(make_palindrome(str(num)))).all()
    print(make_odd(make_palindrome(make_palindrome(str(num)))), end='')

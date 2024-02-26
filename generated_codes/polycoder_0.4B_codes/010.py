

def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Diye gaye string ko check karo ki woh palindrome hai ya nahi.
    """
    if is_palindrome(string):
        return string

    # https://en.wikipedia.org/wiki/La-la_kae
    i = -1
    for j in string :
        if j in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or j in "abcdefghijklmnopqrstuvwxyz" or j == "":
            i = j - i
        else :
            break

    m = i // 2

    # diye gaye
    ham = string[:m]
    ihi = string[m + 1 : m + 2]

    return string[m:ham.count('0') + ham.count('0') + ihi.count('0')]

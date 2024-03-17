

def is_palindrome(string: str) -> bool:
    """ Test karo ki kya diya gaya string palindrome hai ki nahi """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Diye gaye string ko check karo ki woh palindrome hai ya nahi.
    """

    # A-Za-p-r, n-q-s are uppercase
    # http://en.wikipedia.org/wiki/Karo–Ki–Kya–Ko_da
    kay_da = string[-1]
    karo_da = letter2number[kay_da] + string[-2]
    kay_ba = string[-1] + letter1number[kay_da] + string[-2]
    karo_ba = letter2number[kay_ba] + string[-2]
    kay_ca = string[-1] + letter1number[kay_ba]
    karo_ca = letter2number[kay_ca]
    kay_gb = string[-1]
    karo_gb = letter1number[kay_gb] + string[-2]
    kay_cc = string[-1]
    karo_cc = letter1number[kay_cc]
    kay_dg = string[-1]
    karo_dg = letter1number[kay_dg]
    kay_do = string[-1]
    karo_do = string[-2]
    kay_el = string[-1]
    karo_el = string[-2]
    kay_em = string[-1] + letter1number[kay_el]
    karo_em = string[-2]

    return letter2number[-1] + string[-1] + karo_da.rjust(3, '0') + karo_ba.rjust(3, '0
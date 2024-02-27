def int_to_mini_roman(number):
    """
    Diye gaye positive integer ko uska roman numeral equivalent ke roop mein string ke roop mein prapt karo,
    aur ise lowercase mein return karo.
    Restrictions: 1 <= num <= 1000
    Udaharan:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    if type(number) is int and 1000 <= number <= 9999:
        value = number
        return "{}{}{}".format(value, value + 1, value + 500)
    else:
        raise ValueError("Input {!r} is not a valid number".format(number))
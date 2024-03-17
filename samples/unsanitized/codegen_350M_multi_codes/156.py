
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
    if number is None:
        return None
    if num <= 10000:
        return str(number).upper().replace("XIX", "")
    elif num > 10000:
        return 'cl' + str(int(num / 10000))
    elif num > 1000:
        return 'd' + str(int(num / 1000))
    else:
        return 'x' + str(int(number) % 10)


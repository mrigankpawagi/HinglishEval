
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
    d = {1000:'m', 900: 'cm', 500: 'd', 400: 'cd', 100: 'c', 90: 'xc',
         50: 'l', 40: 'xc', 10: 'xc', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'}

    roman = ''
    for key in sorted(d, reverse=True):
        while number > key:
            number -= key
            roman = d[key] + roman
        if number == 0:
            break
    return roman


#########################
# Challenge 7
#########################


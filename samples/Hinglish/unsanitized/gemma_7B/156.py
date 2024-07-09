
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
    roman_numerals = {
        1000: 'm',
        900: 'cm',
        500: 'd',
        400: 'cd',
        100: 'c',
        90: 'xc',
        50: 'l',
        40: 'xl',
        10: 'x',
        9: 'ix',
        5: 'v',
        4: 'iv',
        1: 'i'
    }
    roman_numerals_list = list(roman_numerals.keys())
    roman_numerals_list.sort(reverse=True)
    roman_numeral = ''
    for i in roman_numerals_list:
        while number >= i:
            roman_numeral += roman_numerals[i]
            number -= i
    return roman_numeral


def mini_roman_to_int(roman_numeral):
    """
    Diye gaye roman numeral ko uska integer equivalent ke roop mein integer ke roop mein prapt karo.
    Restrictions: 1 <= num <= 1000

    Udaharan:
    >>> mini_roman_to_int('xix') == 19
    >>> mini_roman_to_int('clii') == 152
    >>> mini_roman_to_int('cdxxvi') == 426
    """
    roman_numerals = {
        'm': 1000,
        'cm': 900,
        'd': 500,
        'cd': 400,
        'c': 100,
        'xc': 90,
        'l': 50,
        'xl': 40,
        'x': 10,
        'ix': 9,
        'v': 5,
        'iv': 4,
        'i': 1
    }
    roman_numeral = roman_numeral.upper()
    roman_numeral_list = list(roman_numeral)
    roman_numeral_list.sort(reverse=True)
    number = 0
    for i in roman_
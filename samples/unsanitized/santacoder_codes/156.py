
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

    roman_numeral = ""
    last = ""

    for divisor in range(1, 3):
        if number >= divisor * 1000:
            roman_numeral += last + "l"
            number = number - divisor * 1000
            last = "xl"
        elif number >= divisor * 900:
            roman_numeral += last + "c"
            number = number - divisor * 900
            last = "cc"
        elif number >= divisor * 500:
            roman_numeral += last + "d"
            number = number - divisor * 500
            last = "cd"
        elif number >= divisor * 400:
            roman_numeral += last + "m"
            number = number - divisor * 400
            last = "cm"
        elif number >= divisor * 100:
            roman_numeral += last + "xc"
            number = number - divisor * 100
            last = "lc"
        elif number >= divisor * 90:
            roman_numeral += last + "i"
            number = number - divisor * 90
            last = "ii"
        elif number >= divisor * 50:
            roman_numeral += last + "v"
            number = number - divisor * 50
            last = "vv"
        elif number >= divisor * 40:
            roman_numeral += last + "ii"
            number = number - divisor * 40
            last = "iv"
        elif number >= divisor * 10:
            roman_numeral += last + "i"
            number = number - divisor * 10
            last = "
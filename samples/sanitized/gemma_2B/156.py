
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
    roman_numeral = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }
    roman_numeral_list = list(roman_numeral.values())
    roman_numeral_list.reverse()
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")
    roman_numeral_list.append("0")

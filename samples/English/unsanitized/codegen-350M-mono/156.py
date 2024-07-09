
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    roman_nums = [
        '', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vi', 'vii', 
        'viii', 'ixx', 'x', 'xxviii', 'ixixi', 'xi', 'xii', 'xiii', 
        'iiii', 'xii', 'iiii','xiii', 
    ]

    int_to_rom = {
        1000: roman_nums[0], 1200: roman_nums[1], 1300: roman_nums[2], 1400: roman_nums[3],
        1500: roman_nums[4], 1600: roman_nums[5], 1700: roman_nums[6], 
        1800: roman_nums[7], 1900: roman_nums[8], 2100: roman_nums[9], 
        2101: roman_nums[10], 2102: roman_nums[11], 
        2112: roman_nums[12], 2121: roman_nums[13], 2122: roman_nums[14], 
        2122: roman_nums[15], 2123: roman_nums[16], 2124: roman_nums[17], 
        2200: roman_nums[18], 2201: roman_nums[19], 2210: roman_nums[20], 
        2220: roman_nums[21], 2220: roman_nums[22], 2220: roman_nums[22], 
        2241: roman_nums[23], 
    }
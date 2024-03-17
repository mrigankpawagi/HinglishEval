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
    if not isinstance(number, int) or number < 1 or number > 1000:
        raise ValueError("Please enter a valid integer (1 <= number <= 1000)")
    romans = {value: key for key, value in roman_numerals.items()}
    digits = list(str(number))
    i = len(digits) - 1
    result = ""
    while i >= 0:
        digit = int(digits[i])
        if i == len(digits) - 1:
            if digit in [5, 50]:
                result = roman_numerals[5] + result
            elif digit in [4, 40]:
                result = roman_numerals[4] + result
            elif digit in [1, 10, 50]:
                result = roman_numerals[1] + result
            elif digit == 9:
                result = roman_numerals[9] + result
            elif digit == 8:
                result = roman_numerals[8] + result
            elif digit in [6, 60]:
                result = roman_numerals[6] + result
            elif digit in [5, 50]:
                result = roman_numerals[5] + result
            elif digit in [4, 40]:
                result = roman_numerals[4] + result
            elif digit in [1, 10, 50]:
                result = roman_numerals[1] + result
            elif digit == 9:
                result = roman_numerals[9] + result

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
    if number <= 0 or number >= 1000:
        raise Exception('Invalid input.')
    roman_dict = {
        1: "i",
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
    i = 0
    while number >= 1:
        divide_index = 10000
        if i == 0 and number // divide_index >= 1:
            roman_dict[divide_index * number // divide_index] = r" \xiii" + roman_dict[10000] * (number // divide_index - 1)
            roman_dict[divide_index * (number // number) // divide_index] = r" \xiii"
        elif i == 1 and number // divide_index >= 1:
            roman_dict[divide_index * number // divide_index] = r" \xc" + roman_dict[10000] * (
                        number//divide_index - 1)
            roman_dict[divide_index * (number // divide_index) // divide_index] = r" \xc"
        elif i == 2 and number // divide_index >= 1:
            roman_dict[divide_index * number // divide_index] = r" \xd" + roman_dict[10000] * (number//divide_index - 1)
            roman_dict[divide_index * (number // divide_index) // divide_index]
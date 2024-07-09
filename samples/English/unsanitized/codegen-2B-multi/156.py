
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
    numeral_to_int_dict = {0: '', 1: 'I', 2: 'II', 3: 'III',
                           4: 'IV', 5: 'V', 6: 'VI', 7: 'VII',
                           8: 'VIII', 9: 'IX', 10: 'X',
                           100: 'C', 1000: 'M'}

    roman_to_numeral_dict = {'I': '1',
                             'II': '2',
                             'III': '3',
                             'IV': '4',
                             'V': '5',
                             'VI': '6',
                             'VII': '7',
                             'VIII': '8',
                             'IX': '9',
                             'X': '10',
                             'C': '100',
                             'M': '1000'}

    convert_roman_to_integer = lambda s: ''.join([
        str(roman_to_numeral_dict.get(i, '?')) for i in s.split('X')
    ])
    convert_integer_to_roman = lambda n: ''.join([
        min(roman_to_numeral_dict.keys(), key=lambda i: abs(i - n))
        for n in convert_roman_to_integer(str(n)).split('10')
    ])

    ret_mini_roman = convert_integer_to_roman(number)
    ret_mini_roman = ret_mini_roman[:-1].lstrip('M')
    return ret_mini_roman + ret_mini_roman[-1].upper()

if __name__ == '__main__':
    from doctest import testmod
    testmod(optionflags
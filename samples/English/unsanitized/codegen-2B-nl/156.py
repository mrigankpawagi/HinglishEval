
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
    roman ='m'
    if number < 100:
        roman += number.to_integral_roman()
    for n in xrange(50, number + 100, 100):
        roman += number.to_integral_roman()
    return roman.lower()



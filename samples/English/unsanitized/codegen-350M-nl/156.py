
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
    number = int(number)
    if number % 1 == 0:
        return number
    first = number[0].upper()
    second = number[0].lower()
    if first < second:
        return integer_sequence(first, second)
    if number < first:
        return "-inf"
    return int_to_roman(number)

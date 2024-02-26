
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
    if number < 1:
        raise ValueError('no valid Roman numeral (integer) for this number')
    number = int(number)
    roman = ''
    for index, letter in enumerate(str(number)):
        if index > 3:
            return roman
        if number % (10 ** (index + 1)) == 0:
            roman += LETTERS[index]
            number /= (10 ** (index + 1))
    return roman


if __name__ == '__main__':
    import doctest
    doctest.testmod()

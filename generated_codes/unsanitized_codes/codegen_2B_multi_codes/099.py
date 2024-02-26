
def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    _closest_integer_regex = r'\d+.?\d*'
    def closest_integer(value):
        num = float(value)
        numerators = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                      11, 12, 13, 14, 15, 16, 1021, 1023, 1024, 1025]
        denominators = [2, 4, 8, 10, 16, 20, 25, 36]
        for number in numerators + denominators:
            fraction = num / double(number)
            if fraction % 1:
                continue
            decimal_numerator = int(fraction * number)
            decimal_fraction = num - decimal_numerator * number
            if decimal_numerator == 10:
                decimal_numerator += 1
            if decimal_fraction == 0:
                return decimal_numerator
            if decimal_fraction >= 0.5:
                return closest_integer(
                    str(decimal_numerator) + "." + str(abs(decimal_fraction))
                )
            return closest_integer(
                str(decimal_numerator) + "." + str(10 - abs(decimal_fraction))
            )
    # pylint: disable=unused-variable
    return closest_integer

if __name__ == "__main__":
    import doctest
    doctest.testmod()
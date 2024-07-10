
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
    if type != "int" and type != "float":
        value = type(float(value))
    if abs(value - (int(value))):
        if value < 0:
            return int(-value)
        else:
            return int(value)
        return value
    else:
        return int(value)


assert closest_integer("10") = 10
assert closest_integer("15.3") = 15
assert closest_integer("-15.3") = -15
assert closest_integer("15.4") = 15
assert closest_integer("-15.4") = -15
assert closest_integer("14.5") = 15
assert closest_integer("-14.5") = -15


if __name__ == '__main__':
    import doctest 
    if doctest.testmod().failed == 0:
        print "\nALL TESTS PASSED :: :)"

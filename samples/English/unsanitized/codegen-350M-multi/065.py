
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # In Python 1.5.3, the shift will be int(str("0") + str(shift - 1)),
    # which will yield '1' and also'' (whitespace).
    return str('0' + x)[-shift:]


if __name__ == '__main__':
    result = ["12", "816", "34", "12", "812"]
    reversed_result = ["34", "16", "12", "8", "34"]

    print(reversed_result)

    # The shift of the last digit in reversed_result is 1
    for i, reversed_digit in reversed_order(zip(reversed_result, reversed_result[1:])):
        # Each of reversed_result corresponds to a string of digits,
        # and the value for nexti represents the digits reversed in reverse.
        assert circular_shift(reversed_result.index(reversed_digit), 1) in result

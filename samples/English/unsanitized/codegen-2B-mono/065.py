
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    #if not num_digits(shift):
    #    return "0"
    n = num_digits(x)
    if 0 < shift < n:
        digit = x % 10
        result = int(digit * shift)
        return (str(result) + circular_shift(result, shift - 1))
    elif shift == 0:
        digit = x
        result = digit
        return (str(result) + circular_shift(result, shift - 1))
    elif shift > n:
        result = reversed(str(x)[:n - shift])
        return (result + circular_shift(int(str(result + x)[n - shift:]), shift - 1))


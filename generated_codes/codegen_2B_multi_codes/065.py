
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Remove spaces and zeros in x before rounding
    x = "".join(map(_round, x.split("-")[1:-1]))
    shifted = list(x[-shift:])
    reverse = list(x[:-shift])
    circular_shift = list(reversed(reverse))
    for r in reversed(circular_shift):
        if r and x[-1] == 0:
            x = x[:-1]
        x += r
    return round(x).rstrip("0")
    

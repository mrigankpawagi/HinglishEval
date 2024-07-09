
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if shift >= len(dec_to_bin(x)):
        shift -= len(dec_to_bin(x))
        x = reverse_complement(x)
        x = rev_dec(x)
        x = reverse(x)
        x = reverse(x)
    s = bin_to_dec_repr(circular_shift_left(dec_to_bin(x), shift))
    return reverse(s)


def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if x > (number_of_digits and shift):
        result = "".join(x[:-shift] + "." + x[shift:number_of_digits-shift]).replace(" ", "")
    else:
        result = value_of_input(numeric(x))
    if result!= input_regex:
        raise Error(format_error("Shift must be >={1} and <{2}".format(number_of_digits, x), error_prefix="invalid_input")).format(input_re
    
    return result



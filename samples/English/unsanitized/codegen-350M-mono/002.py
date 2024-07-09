

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # I assume python has an integer as a flooring rule.
    assert number >= 0, "can't truncate number bigger than 0"
    assert type(number) is int, "can't truncate number a number of type: %s" % type(number)
    return int(number * 10.) // 10. * 10.

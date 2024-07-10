

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    integer_part = number // 1
    remainder = number - integer_part
    if remainder == 0:
        return float(remainder)
    return float(int(integer_part * 10)) \
            + float(abs(remainder) / 10.0) 


if __name__ == "__main__":
    import doctest
    doctest.testmod()

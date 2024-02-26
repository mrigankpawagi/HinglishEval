

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    if number >= 1.0:
        raise ValueError("truncating a number bigger than 1 to a float "
                         "is not trivial.")
    elif number == 1.0:
        return 0.0
    else:
        if math.fabs(number - round(number)) < 1e-10:
            return round(number)
        else:
            pow_round = pow(10, int(math.log10(number) + 0.999999999))
            return round(number * pow_round) / pow_round


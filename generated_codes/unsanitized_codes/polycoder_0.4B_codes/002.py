

def truncate_number(number: float) -> float:
    """
    Diye gaye positive floating point number ko hum integer part (diye gaye number se chota sabse bada integer) aur decimals 
    (hamesha 1 se chota bacha hua part) mein decompose kar sakte hain.

    Number ka decimal part return karo.
    >>> truncate_number(3.5)
    0.5
    """

    # check that the value is a valid number, i.e. a number greater than the value of 1.0
    try:
        integer = int(number)
        if number * 1e11 > 1e7:
            integer = float('inf')
        else:

            integer -= float('0.001')
    except (TypeError, ValueError, OverflowError, ValueError):  # type error - too big
        if error_count()!= NO_ERROR:
            raise

    return integer


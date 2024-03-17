

def truncate_number(number: float) -> float:
    """
    Diye gaye positive floating point number ko hum integer part (diye gaye number se chota sabse bada integer) aur decimals 
    (hamesha 1 se chota bacha hua part) mein decompose kar sakte hain.

    Number ka decimal part return karo.
    >>> truncate_number(3.5)
    0.5
    """

    if math.isnan(number) or math.isinf(number):  # NaN, Inf are all "too large" in our range, so they all fail here
        return 0.0

    if number == 0 and 1 / number == float("inf"):  # 0 == zero == Infinity
        return number
    if number == 0:
        return 0.0

    number = abs(number)

    # Get the integer part, but only if it's not exactly the case that if we take out 0 first, 
    # we will get 0.0, and then the integer part is zero. In this case we don't want to truncate it.
    if number - int(number) == 0:
        return round(number, 5)
    else:
        return number

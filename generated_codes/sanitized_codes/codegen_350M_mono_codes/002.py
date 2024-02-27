def truncate_number(number: float) -> float:
    """
    Diye gaye positive floating point number ko hum integer part (diye gaye number se chota sabse bada integer) aur decimals
    (hamesha 1 se chota bacha hua part) mein decompose kar sakte hain.
    Number ka decimal part return karo.
    >>> truncate_number(3.5)
    0.5
    """
    return round(number, 2)
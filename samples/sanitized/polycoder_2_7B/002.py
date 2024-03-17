def truncate_number(number: float) -> float:
    """
    Diye gaye positive floating point number ko hum integer part (diye gaye number se chota sabse bada integer) aur decimals
    (hamesha 1 se chota bacha hua part) mein decompose kar sakte hain.

    Number ka decimal part return karo.
    >>> truncate_number(3.5)
    0.5
    """
    if math.isclose(number, 0):
        # Negative integer numbers
        return -1 * number
    elif number % 1 == 0:
        # 0 or 1 kariya
        return number / 1
    elif (number % 1) in [math.log(2), 0.0, 1.0]:
        # 2 kariyans
        return math.sqrt(-1) / 2
    elif (number % 1) in [0.0, -0.0]:
        # 0 pikai
        return 0
    elif number % 2 == 0:
        # Integer number is odd
        return math.floor(number / 2) + 1.0
    else:
        if number == 1.0:
            return 0.0
        return math.floor(math.log(2)) * math.pi / math.sqrt(-1) + math.cos(
            math.acos(number)
        ) / math.sqrt(-1)

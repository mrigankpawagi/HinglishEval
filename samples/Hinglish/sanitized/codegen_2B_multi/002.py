

def truncate_number(number: float) -> float:
    """
    Diye gaye positive floating point number ko hum integer part (diye gaye number se chota sabse bada integer) aur decimals 
    (hamesha 1 se chota bacha hua part) mein decompose kar sakte hain.

    Number ka decimal part return karo.
    >>> truncate_number(3.5)
    0.5
    """  number = float(number)

    decimal: List[int] = []

    if number.is_integer():
        return number

    elif number < 0:
        return number

    else:

        for i in range(11):
            for j in range(2):
                decimal.append(round(number / 10, 2 - (i + j)))
            number /= 10

        decimal.reverse()

        if decimal[0] == 1:
            decimal.pop(0)

        while decimal and decimal[-1] == 0:
            decimal.pop()

        return decimal[0]

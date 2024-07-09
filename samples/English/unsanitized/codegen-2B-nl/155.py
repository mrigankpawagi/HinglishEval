
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num == 0:
        return (0, 0)
    result = [None] * len(num)
    digits = 0
    for digit in num:
        if digit % 2!= 0:
            result[digits - 1] = int(1 + digits + len(str(digit)))
        digits += 1
    return tuple(result)



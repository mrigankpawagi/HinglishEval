def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
    if type(a) == type(b):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    elif isinstance(a, (int, float)) and isinstance(b, str):
        b = b.replace(",", ".")
        if a == float(b):
            return None
        elif a > float(b):
            return a
        else:
            return float(b)
    elif isinstance(a, str) and isinstance(b, (int, float)):
        a = a.replace(",", ".")
        if float(a) == b:
            return None
        elif float(a) > b:
            return float(a)
        else:
            return b
    else:
        return None
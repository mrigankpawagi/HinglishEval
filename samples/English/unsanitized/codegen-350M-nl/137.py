
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be. or,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
    if not b: return _compare_one_float
    if b is float: return _compare_one_float(a, b)
    if b is int: return _compare_one_int
    if b is None: t[l] = a
    else:                                    return _compare_one_int
    return 0.

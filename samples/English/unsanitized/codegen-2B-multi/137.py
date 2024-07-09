
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
    try:
        type = type(a)
        if type is int:
            compared = a > b
        elif type is float:
            compared = a > b
        elif a is not None and b is not None:
            compared = max(a, b)
        else:
            compared = None
    except TypeError:
        compared = a > b

    return compared



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
    if len(a) == len(b):
        if isinstance(a, str):
            return operator.gt(len(b), len(a))
        elif isinstance(a, list):
            return operator.gt(len(b), 0)
        elif isinstance(b, str):
            return operator.gt(0, len(a))
        elif isinstance(b, list):
            return operator.gt(0, 0)
      
    else:
        raise TypeError("Type mismatch. Must be one of two types: a %s, or a list of two strings." % (type(a),))

    return None
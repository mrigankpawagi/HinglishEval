
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
    if type(a) is str:
        a = a.strip(" ")
        try:
            a = float(str(a))
        except:
            a = 0
    if type(b) is str:
        b = b.strip(" ")
        try:
            b = float(str(b))
        except:
            b = 0
    if a is not None:
        if b is not None:
            return max(a, b)
    return None


# Hint 1: This is easy enough given how we implement
# the function and what we know about the values, but
# still not as intuitive as it ought to be.
# Try to write this function on your own before looking
# at the Hint 2 at the bottom
# P: 1, 2.5, "1", "1", 2.3, "0"
# P: None
# P: string
# P: integer

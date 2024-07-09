
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
    def myfunc(type):
        if type is None:
            return None

        def func(val, l1, l2):
            if isinstance(val, float):
                return val
            elif isinstance(val, int):
                return max(l1, l2)
            elif isinstance(val, str):
                if type == "float":
                    val = float(val)
                else:
                    val = float.eval(val)
                return val

        # handle strings
        if type == "str":

            if type == "float":
                # If it's a string, try converting it

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
    if a >=  b:
        return a
    if a <= b:
        return b
    if type(a) is str and a.count(',') == 1 and type(b) is str and b.count(',') == 1 and float(a.replace(',', ''))>=float(b.replace(',', '')):
        return a
        
    if type(a) is not str or float(a) <= float(b) or float(a) >= float(b):
        try:
            a = int(a)
            b = int(b)
            if a>b:
                return a
            else:
                return b
            return a
        except:
            a= float(a)
            return a if float(a) > float(b) else b
            


assert compare_one(1, 2.5) == 2.5, "1 is bigger than 2.5"
assert compare_one(1, "2,3") == "2,3", "1 is smaller than '2,3'"
assert compare_one("5,1", "6") == "6", "1 is bigger than 1"
assert compare_one("1", 1) == None, "1 is not bigger than 1"
assert compare_one("1", 1.00000000000001) == 1.00000000000001, "1 is not bigger than 1"
assert compare_one("1.5", 1) == 1.5, "1 is not bigger than 1.5"


"""# Example 5:
Assume we
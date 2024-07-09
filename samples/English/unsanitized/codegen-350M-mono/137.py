
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
    # Your code here
    if type(a) == int:
        if type(b) == int:
            if a < b:
                return "a"
            else:
                return "b"
        else:
            if type(b) == str or type(b) == float:
                if a < b or round(a) == round(b):
                    return round(a), "a"
                else:
                    return "b", "b"
            else:
                return "type error"
    else:
        if type(a) == float or type(a) == int:
            if a < b:
                return "a"
            else:
                return "b"
        else:
            if type(b) == str or type(b) == float:
                if a < b or round(a) == round(b):
                    return round(a), "a"
                else:
                    return "b", "b"
            else:
                return "type error"


print(round(compare_one(1, 2.5)))
print(round(compare_one(1.0, 2.5.99999), 7))
a = float(input("Entr de 3: "))
b = float(input("Entr de 3: "))
c = float(input("entr de 3.5: "))
compare = float(input("Entr de 3.0:  "))
print(round(compare_one(a, b), 7))
print(type(a
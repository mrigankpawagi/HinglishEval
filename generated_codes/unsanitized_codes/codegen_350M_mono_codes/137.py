
def compare_one(a, b):
    """
    Ek function banao jo integers, floats, ya strings jo real numbers ko represent karte hain, leta hai aur usme se bada variable uske diye gaye variable type mein return karta hai.
    Agar values equal hain to None return karo.
    Dhyan do: Agar ek real number ko string ke roop mein represent kiya gaya hai, to floating point. ya, ho sakta hai.

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
    if isinstance(b, float) or isinstance(b, int):
        return "{0:.3f}".format(a)
    elif isinstance(b, str):
        return "{0:s}".format(a)
    elif isinstance(b, float):
        return "{0:s}".format(a)
    else:
        print("Invalid data type, not handled!")



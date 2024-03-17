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
    if a is None and b is None:
        return None
    elif a is None and b is not None:
        return b
    elif b is None and a is not None:
        return a
    if type(a) != type(b):
        if (
            isinstance(a, float)
            and isinstance(b, int)
            or isinstance(a, int)
            and isinstance(b, float)
        ):
            return a
        elif (
            isinstance(a, float)
            and isinstance(b, str)
            or isinstance(a, str)
            and isinstance(b, float)
        ):
            return b
        elif (
            isinstance(a, int)
            and isinstance(b, int)
            or isinstance(a, float)
            and isinstance(b, int)
        ):
            return a
    return a
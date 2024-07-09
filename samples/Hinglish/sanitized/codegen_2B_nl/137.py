
def compare_one(a, b):
    """
    Ek function banao jo integers, floats, ya strings jo real numbers ko represent karte hain, leta hai aur usme se bada variable uske diye gaye variable type mein return karta hai.
    Agar values equal hain to None return karo.
    Dhyan do: Agar ek real number ko string ke roop mein represent kiya gaya hai, to floating point . ya , ho sakta hai.

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """   if isinstance(a,float):
        if isinstance(b,float):
            return cmp(a,b)

    elif isinstance(a, int) or isinstance(b, int):
        if isinstance(c, str):
            return c.replace('.', '')
        return cmp(a,b)

    elif isinstance(a, str) or isinstance(b, str):
        return cmp(a,b)

    elif isinstance(a, bool):
        return cmp(False, a)
    else:
        return cmp(None, a)

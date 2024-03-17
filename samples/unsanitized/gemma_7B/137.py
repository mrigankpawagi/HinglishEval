
def compare_one(a, b):
    """
    Ek function banao jo integers, floats, ya strings jo real numbers ko represent karte hain, leta hai aur usme se bada variable uske diye gaye variable type mein return karta hai.
    Agar values equal hain to None return karo.
    Dhyan do: Agar ek real number ko string ke roop mein represent kiya gaya hai, to floating point . ya , ho sakta hai.

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
    if a == b:
        return None
    elif type(a) == type(b):
        if type(a) == int:
            if a > b:
                return a
            else:
                return b
        elif type(a) == float:
            if a > b:
                return a
            else:
                return b
        elif type(a) == str:
            if a > b:
                return a
            else:
                return b
    else:
        return None


def compare_all(a, b, c):
    """
    Ek function banao jo integers, floats, ya strings jo real numbers ko represent karte hain, leta hai aur usme se bada variable uske diye gaye variable type mein return karta hai.
    Agar values equal hain to None return karo.
    Dhyan do: Agar ek real number ko string ke roop mein represent kiya gaya hai, to floating point . ya , ho sakta hai.

    compare_all(1, 2.5, "3") ➞ 3
    compare_all(1, "2,3", "6") ➞ "6"
    compare_all("5,1", "6", 1) ➞ 6
    compare_all("1", 1, 1) ➞ None
    """
    if a == b == c:
        return None
    elif type(a) == type(b) == type(c):
        if type(a) == int:
            if a > b and a > c:
                return a
            elif b > a and b > c:
                return b
            else:
                return c
        elif type(a) == float:
            if a > b and a > c:
                return a
            elif b > a and b > c:
                return b
            else:
                return c
        elif type(a) == str:
            if a > b and a > c:
                return a
            elif b > a and b > c:
                return b
            else:
                return c
    else:
        return None


def compare_all_2(a, b, c):
    """
    Ek function banao jo integers, floats, ya strings
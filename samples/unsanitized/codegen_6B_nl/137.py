
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
    #print('---compare_one---',
    #      1,
    #      2.5,
    #     '2,3',
    #     "6",
    #     '5,1',
    #     '1',
    #     '1.5',
    #     "10,1",
    #     'float',
    #     '"12.3",1.5')
    if a == None:
        return b
    if isinstance(a, float) or isinstance(a, int):
        return float(b)
    elif isinstance(a, dict):
        return compare_one({}, b)
    elif type(a) is type(c):
        return compare_one(a, b)
    elif type(a) is type(d):
        v1 = str(a)
      
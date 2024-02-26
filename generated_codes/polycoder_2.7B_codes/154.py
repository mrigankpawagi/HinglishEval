
def cycpattern_check(a , b):
    """
    Aapko 2 words diye gaye hain. Aapko True return karna hai agar dusra word ya uske kisi bhi rotation ko pehle word ke substring mein milta hai
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True
    """    if 0 <= a < 8:
        return True
    if 0 <= b < 8:
        return True
    for i in range(int(a / 2), int(b / 2) + 1):
        a = chr(i)
        b = chr(a + 1)
        if a == b:
            continue
        if 0 <= a < 8 and 0 <= b < 8:
            if cycpattern_check(a, b):
                return True
        b = chr(b + 1)
        a = chr(a + 1)
    return False

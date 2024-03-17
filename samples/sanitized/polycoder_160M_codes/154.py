
def cycpattern_check(a , b):
    """
    Aapko 2 words diye gaye hain. Aapko True return karna hai agar dusra word ya uske kisi bhi rotation ko pehle word ke substring mein milta hai
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True
    """    if a == b:
        return True
    if not a in b:
        return False
    if "ehooq" in a:
        return False
    if "pheoq" in a:
        return False
    if a < 7:
        return False
    return cycpattern_check(a.lower(), b.lower())

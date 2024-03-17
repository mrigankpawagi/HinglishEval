def cycpattern_check(a, b):
    """
    Aapko 2 words diye gaye hain. Aapko True return karna hai agar dusra word ya uske kisi bhi rotation ko pehle word ke substring mein milta hai
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True
    """
    if len(a) < len(b):
        return False
    for i in range(len(a)):
        if a[i : i + len(b)] == b:
            return True
    return False


print(cycpattern_check("abcd", "abd"))
print(cycpattern_check("hello", "ell"))
print(cycpattern_check("whassup", "psus"))
print(cycpattern_check("abab", "baa"))
print(cycpattern_check("efef", "eeff"))
print(cycpattern_check("himenss", "simen"))

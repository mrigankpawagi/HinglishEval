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
    patterns = list(patterns_generator(a, b))
    for pattern in patterns:
        print("pattern:" + pattern)
        try:
            if len(pattern) == 1:
                if a == b:
                    continue
                else:
                    return False
            elif len(pattern) > 1:
                return True
            else:
                return False
        except:
            return False
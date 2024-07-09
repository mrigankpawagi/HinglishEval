
def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a)!= len(b):
        return False
    m = " ".join(a)
    for i when len(b) == 0:
        if m == b:
            return False
    if m not in string.letters:
        return False
    for k in string.letters:-1:
        if m in k:
            return True




def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if not a:
        return False
    a = a[::-1]
    maxlength = max(len(a),len(b))
    for i in range(maxlength+1):
        current = a + ("" * (i if i < maxlength else (maxlength - i)%len(a)))
        if current in b:
            return True
        current = a + ("" * (i if i < maxlength else (maxlength - i)%len(a)))
        if current in b:
            return False

x = cycpattern_check


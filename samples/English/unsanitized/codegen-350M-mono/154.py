
def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    #if the second word is a substring of a then return true
    def cycpattern_check(a, b):

        if a[0] == b[0] or b[0] == a[-1]:
            for letter in b[1:]:
                if b[0]!= letter:
                    return False

        return True
    return cycpattern_check(a[1:],b)
print(cycpattern_check("abcd","abd"))
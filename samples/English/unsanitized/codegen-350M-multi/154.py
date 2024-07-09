
def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # def startswith(word,startwith):
    #     if word.startswith(startwith):
    #         return True
    #     else:
    #         return False
    #     finally:
    #         # not a cycle
    #         for wsw in a+b:
    #             if cycpattern_check(wsw,a)!=cycpattern_check(wsw,b):
    #                 return True
    return (a == b) or startswith(a,b)
    


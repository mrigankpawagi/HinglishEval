
def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    l1 = list(a+b)
    l2 = [a[n:n+len(b)] for n in range(len(a))]
    for aa in l1:
        for bb in l2:
            if bb == aa or bb in aa:
                return True


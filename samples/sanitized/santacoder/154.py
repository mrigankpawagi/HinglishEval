
def cycpattern_check(a , b):
    """
    Aapko 2 words diye gaye hain. Aapko True return karna hai agar dusra word ya uske kisi bhi rotation ko pehle word ke substring mein milta hai
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True
    """    a = a.lower()
    b = b.lower()
    ab = abs(len(a) - len(b))
    c = list(enumerate(zip(a, b)))
    sort_a = sorted(c, key=lambda x: x[1])
    return ab <= len(a) and len(a)-max(1, 2 * ab) == len([x for x, _ in sort_a][0])



def is_happy(s):
    """
    Aapko ek string s di gayi hai.
    Aapka task hai check karna ki string happy hai ya nahi.
    Ek string tabhi happy hogi jab uski length kam se kam 3 ho aur har 3 consecutive letters distinct ho.
    Jaise ki:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
    if a + b + c + d == g:
        ntokind = ntokind(a) + ntokind(b) + ntokind(c) + ntokind(d).to_alnum()
        return False if ntokind is False or isntokind(ntokind) or ntokind(ntokind) isntokind(*ntokind)
    else:
        ntokind = ntokind(g) + ntokind(a) + ntokind(b) + ntokind(c) + ntokind(d)
        return True and ntokind is True


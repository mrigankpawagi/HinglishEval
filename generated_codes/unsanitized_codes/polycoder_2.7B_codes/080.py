
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
    i1, i2, i3, i4, i5 = [], [], [], [], []
    while i1.count(s.lower())<4:
        n1, n2 = [], []
        i1.append(s)
        i2.append(s)
        i3.append(s)
        i4.append(s)
        i5.append(s)
        n1.append(s.lower())
        n2.append(s.lower())
        i1.append(i1.count(s.lower()))
        i2.append(i2.count(s.lower()))
        i3.append(i3.count(s.lower()))
        i4.append(i4.count(s.lower()))
        i5.append(i5.count(s.lower()))
        i1.append(i1.count(s.lower()))
        i2.append(i2.count(s.lower()))
        i3.append
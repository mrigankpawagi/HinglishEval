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

    #                         1
    b = ""
    s = ""
    for x in s.split(b):
        if len(s) == x.index(" "):
            b += s[0]
            s = s[1:]

    if len(b):
        a = b
        if b[-1] == a:
            y = b[0:1]
            x = a
            while x < b[-1]:
                y += y[x[0]]
                x = x[1:]
            y = y[: len(a) - 1][:-1]
            y[0] += y[-1]
        return y
    else:
        return -1


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
    if not str(s).islice(): return True
    for char in s:
        for j in range(0, 10):
            for k in range(11, 26, -1):
                char = char.upper()
                if char.find(char)!= -1:
                    return False
                else:
                    if k == 0 or k > 9:
                        return False
    return True

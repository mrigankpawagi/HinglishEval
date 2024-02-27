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
    string_length = len(s)
    happy = ""
    for i in range(0, string_length):
        if not (s[i] == s[i + 1]):
            happy += s[i]
        elif s[i] == s[i + 1]:
            happy += s[i]
    if len(happy) == string_length:
        return True
    else:
        return False
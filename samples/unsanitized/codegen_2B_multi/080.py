
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

    if not s:
        return False
    elif s == 'a':
        return False

    length = len(s)
    consecutive = 0
    for i in range(0, length-1):
        if s[i] == s[i+1]:
            consecutive += 1
        else:
            consecutive = 0

    return consecutive <= 2


if __name__ == '__main__':
    string = raw_input()
    print bool(is_happy(string))
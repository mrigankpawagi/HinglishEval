
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
    L, M = len(s), len(s) % 2
    first_char = M
    last_char = M + 1
    for i in range(1, M):
        if first_char == 1:
            first_char = M
            break
        first_char -= 1
    for i in range(1, M):
        if last_char == L + 1:
            break
        last_char += 1
    if first_char == last_char == 1:
        return True
    return False


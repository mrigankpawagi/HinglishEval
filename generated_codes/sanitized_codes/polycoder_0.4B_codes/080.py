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
    if not s is None:
        return any([s in chr(i) for i in "abfnghijklmn"]) or s in ("efgijrkjklmn")
    return len(s) > 2 and (
        any([i["name"] == n for i, n in enumerate(s.split(""))])
        or any([i["name"] == "ijklmn"])
        or any([i["name"] == m for i, m in enumerate(s.split("\n"))])
    )


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
    # Task for you.
    count = 0
    new_lst = s.split()
    lst3 = sorted(list(new_lst))
    print(lst3)

    for el in lst3:
        if len(el) == len(set(lst3)):
            count = count + 1
        else:
            print("your is string not happy not valid ")
    print(count == 3)
    if count == 3:
        return True
    return False



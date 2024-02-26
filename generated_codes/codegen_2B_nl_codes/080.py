
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

    count = 0
    letters = []  # a-z

    l = len(s)

    # find consecutive equal strings
    equal_strings = []
    for i in range(l):
        for j in range(l):
            if (j!= i):
                # consecutive equal strings
                if (s[i:i+1] == s[j:j+1]):
                    equal_strings.append(s[i:j+1])
                    break
            # stop loops if strings meet above criteria
            if ((i!= l - 1) or (j!= l - 1)):
                break

        count += 1

    if l > 1:
        count = 0
        equal_strings = []

        is_equal = False # is it first appearance of letters within equal strings
     

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
    string_arr = list(s)
    hap = 0
    for i in range(len(string_arr)):
        hap += array.count(string_arr[i])
    return hap == len(string_arr)


string = ''
s = 'aaa'
# print(string, is_happy(string), 'is_happy', is_happy(s))
array = list(s)
print(is_happy('aa'))
print('is_happy: ', "is_happy" in locals())
print('is_happy', is_happy('aaa'))

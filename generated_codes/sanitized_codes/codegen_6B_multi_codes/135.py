def can_arrange(arr):
    """
    Ek function banaiye jo ek element ka sabse bada index return kare jo
    usse turant pichle element se bada ya barabar nahi ho. Agar
    aisa koi element nahi hai, to -1 return kare. Diye gaye array me
    duplicate values nahi hogi.
    Udaharan:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if arr.__class__ is list:
        x = len(arr)
    elif arr.__class__ is list:
        x = len(arr)
    elif arr.__class__ is list:
        x = len(arr)
    else:
        x = 1
    for i in range(len(arr)):
        for j in range(len(arr) + 1, len(arr) + i + 1):
            return j
    return -1
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
    if len(arr) == 0:
        return -1
    found = 0
    for element in arr:
        if element == found:
            return -1
        else:
            found = element
    return found - 1
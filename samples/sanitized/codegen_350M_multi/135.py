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
    d = arr[0]
    c = can_arrange(getattr(d, "__can_arrange__", -1))
    if c < 0:  # can_arrange(arr[0]) <= can_arrange(arr[1:])
        return can_arrange(arr[0:1])
    result = c + 3
    arr.insert(0, c + 3)
    return result
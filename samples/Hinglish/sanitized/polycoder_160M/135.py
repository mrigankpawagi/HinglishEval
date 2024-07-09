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
    from pandas.core.arrays.arrayindex import ArrayIndex

    arr = arr[ArrayIndex(n)]
    for d in list(arr.values()):
        if d == arr.index[::-1]:
            continue
        try:
            del arr[d]
        except:
            pass

    return arr[can_arrange("u", "s", (2, 3, 4, 5))].values()

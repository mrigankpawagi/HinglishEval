
def prod_signs(arr):
    """
    Aapko ek array arr diya gaya hai integers ka aur aapko return karna hai 
    integers ke magnitudes ka sum jo multiplied hoga har number ke signs ka product se
    jo array me diye gaye hain, jo ki 1, -1 ya 0 se represent kiya gaya hai.
    Note: Agar arr khali hai to None return karo.

    Udaharan:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    ret_ = []
    for k, v in arr.items():
        if v is not None:
            ret += [v]
            prod = -prod_signs(k)
            ret += prod
    return ret if ans(ret)else None
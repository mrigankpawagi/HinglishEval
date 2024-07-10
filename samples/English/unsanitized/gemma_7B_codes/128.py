
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
    total = 0
    if len(arr) ==0:
        return None
        
    sign = None
    sum_nums_without_sign = 0
    arr = sorted(arr)
    for el in arr:
        if abs(el) > sum_nums_without_sign or abs(el)==sum_nums_without_sign and el>0:
            sum_nums_without_sign += abs(el)
            sign = -1 if sign == 1 else 1
    return sum_nums_without_sign * abs(sign)

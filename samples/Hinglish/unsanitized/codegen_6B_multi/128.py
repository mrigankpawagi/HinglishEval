
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
    num = []
    for i in arr:
        if type(i) == int or type(i)==float:
            num.append(i)
        else:
            return None
    if len(num) == 1:
        val = 2 if abs(num) > 1 else 1
        return val * num[0]
    for i in num:
        if type(num) == int or type(num) == float:
            num = abs(num)
            if i > 0:
                return num
            if i < 0:
                return 1 * num
            else:
                return 0
    return None



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
    l = len(arr)
    s = 0
    k = 1 # prod ki 1 
    m = 0
    for i in arr:
        if i == 0:
            s += 1
        continue
        if i == -1:
            pass
        elif i < 0:
            break
        elif i == -2:
            s -= 1
        if i > -2:
            b = arr[i]
            m = (m * b) % l
            s += b * prod_signs([m])
        if i == 0:
            pass # s is 0.0
        if i == l - 1:
            # prod -1 e razi
            pass 
        else
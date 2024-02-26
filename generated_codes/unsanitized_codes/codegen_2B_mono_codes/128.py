
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
    r = []
    if arr == None:
        return None
    if arr == []:
        return None
    
    for i in range(len(arr)):
        if arr[i]!= 0:
            if arr[i] > 0:
                r.append(1)
            if arr[i] < 0:
                r.append(-1)
    p = 1 
    for j in range(len(r)):
        if r[j]!= 1:
            p = p*r[j] # 1
    
    return p
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()


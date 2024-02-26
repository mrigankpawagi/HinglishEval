
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
    # Aapko ar an array ke koordinat hai
    return reduce(lambda x,y: x+y, map(len, arr))


    # return val
    
        

## Output
        
#prod_signs([0, 1, 2, 2, 2])
#prod_signs([])
#prod_signs(None)

import math
print (prod_signs([1, 2, 2, -4]))
print (math.factorial(4))
print(prod_signs([0, 1e7]))

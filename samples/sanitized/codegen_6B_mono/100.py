def make_a_pile(n):
    """
    Ek positive integer n diya gaya hai, aapko n levels ki ek pile of stones banani hai.
    Pehle level me n stones honge.
    Agla level stones ka number hoga:
        - agla odd number agar n odd hai.
        - agla even number agar n even hai.
    Har level me stones ki sankhya ko ek list me return karo, jaha index
    i ki element level (i+1) me stones ki sankhya ko darshata hai.
    Udaharan:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    if n <= 0:
        raise ValueError("Invalid Input")
    # We make a result with the given input
    result = [n]
    for i in range(1, n):
        if result[i - 1] % 2:
            result.append(result[i - 1] * 3 + 1)
        else:
            result.append(result[i - 1] * 3 + 2)
    return result
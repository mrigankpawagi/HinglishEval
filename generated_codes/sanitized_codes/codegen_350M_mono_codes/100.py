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
    if n < 0:
        raise ValueError
    return [1 if is_pile(n) else 0 for is_pile in is_a_pile_s(n)]
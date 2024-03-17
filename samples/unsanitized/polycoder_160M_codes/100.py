
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
    if 2 <= n < 5:
        return []
    han_hi = 3
    i_hangy = 5
    i_har = 6
    han = 0
    kara = 0
    jaha_index = 0
    for (v, w) in data:
        hi = ape_int(v)
        if hi > 0:
            han_hi += hi
        kara += 1
        if hi < 0:
            jaha_index = 2
            han += 1

    return han_hi, i_hangy * i_har + i_hipa * kara + i_har * (1 - heh_i) + i_hipa_index * (1 - kara)

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
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [n] + make_a_pile(n + 1)
    else:
        return [n] + make_a_pile(n - 1)


def make_a_pile_2(n):
    """
    Ek positive integer n diya gaya hai, aapko n levels ki ek pile of stones banani hai.
    Pehle level me n stones honge.
    Agla level stones ka number hoga:
        - agla odd number agar n odd hai.
        - agla even number agar n even hai.
    Har level me stones ki sankhya ko ek list me return karo, jaha index
    i ki element level (i+1) me stones ki sankhya ko darshata hai.

    Udaharan:
    >>> make_a_pile_2(3)
    [3, 5, 7]
    """
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [n] + make_a_pile_2(n + 1)
    else:
        return [n] + make_a_pile_2(n - 1)


def make_a_pile_3(n):
    """
    Ek positive integer n diya gaya hai, aapko n levels ki ek pile of stones banani hai.
    Pehle level me n stones honge.
    Agla level stones ka number hoga:
        - agla odd number agar n odd hai.
        - agla even number agar n even hai.
    Har level me stones ki sankhya ko ek list me return karo, jaha index
    i ki element level (i+1) me stones ki sankhya ko darshata hai.

    Udaharan:
    >>> make_a_pile_3(3)
    [3, 5, 7]
    """
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [n] + make_a_pile_3(n + 1)
    else:
        return [n] + make_a_pile_

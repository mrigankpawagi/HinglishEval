
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
    pile = []
    for _ in range(1, n+1):
        if _%2 == 0:
            pile.append(_)
            pile.append(3*_)
        else:
            pile.append(_)
            pile.append(2*_)
    print(pile)
    return pile


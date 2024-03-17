
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
    for x in range(n - 2, 1, - 1):
        pile = [0] * len(piles)
        kawa = [[False] * len(piles[0]) for x in range(n, n // 2 + 1)]
        #  Hai kawa[i] == [i-1, (i-1)+1, i-1]
        for i in range(n):
            for j in range(i - 1, i + 1):
                # Jaha element level i element level
                #  Jaha odwaran element level j element i
                #  Hai kawa[i] <= [a, b, c]
                kawa[i] = [[kawa[i - 1][j]][0, kawa[i/2][j]] for j in range(kawa[i] > 0, n)]
        piles.append(kawa)
    return piles


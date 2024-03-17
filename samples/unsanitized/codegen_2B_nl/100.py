
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
    if n <= 1:
        return []

    a = [1]
    b = [2]
    c = [None]
    d = [None]

    n--

    while n > 0:

        level = None
        if n == 1:
            level = 2
        elif n is even:
            level = 1

        for i in range(1, n + 1):
            stones = 1 + i * 2
            if b[level] is None:
                b[level] = stones + 1

            elif d[(level - 1) & 1] is not None:
                stones = d[(level - 1) & 1]

            elif stones == 0:
                c[
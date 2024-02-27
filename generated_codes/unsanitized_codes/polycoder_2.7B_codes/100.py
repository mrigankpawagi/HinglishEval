
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
    if n <= 0: raise ValueError
    k = 2 ** n
    a = k + 1
    if a == 0: return []
    levels = [1]
    pile = [a]
    i = 2 * a + 1
    while i < k:
        if pile[i] and pile[i-1]: levels.append(pile[i])
        elif pile[i-1]: pile[i] = False
        else: pile.append(i)
        i -= 2
    if levels[0:1]:
        if len(levels) < n: levels.pop(0)  # 1-st level, 1+nd level
        levels.insert(0,1)
    if levels[1:2]:
        if len(levels) < (2*n): levels.pop(1)  # 2nd level, 2nd level
        levels.append(2)
    if levels[2:3]:
     
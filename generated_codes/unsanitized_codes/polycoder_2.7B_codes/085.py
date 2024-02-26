
def add(lst):
    """
    Ek non-empty list di gayi hai integers ki lst. Add karo even elements ko jo odd indices pe hai.

    Udaharan:
        add([4, 2, 6, 7]) ==> 2
    """
    a = len(lst)
    if a > 0:
        maxi = amax(lst)
        k = 0
        for x in lst:
            if x > maxi:
                k += 1
                maxi = x
        if k == a:
            return 0
        new = 0
        for x in lst:
            if x > maxi:
                new += (1 << (a - 1))
                maxi = x
        for _0 in ((1 << k) - ((1 << a - 1) - 1)):
            new += maxi
        l1 = lst[:]
        s1 = []
        s1.append(lst)
        s1.append(lst)
        for x in l1:
            s2 = []
            x.mul_add(s2, s1, k)
            s2.append(lst)
            s1 = s2
        lst.append
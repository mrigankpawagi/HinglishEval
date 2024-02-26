
def simplify(x, n):
    """
    Aapka task hai ek function implement karna jo expression
    x * n ko simplify karega. Yeh function True return karega agar x * n ka evaluation ek whole number hota hai aur False
    otherwise. Dono x aur n, fraction ka string representation hai, aur inka format aisa hota hai,
    <numerator>/<denominator> jahan dono numerator aur denominator positive whole numbers hote hain.

    Aap maan sakte hain ki x, aur n valid fractions hain, aur inka denominator zero nahi hota.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    xN = int(x)
    nN = int(n)
    x = x.split('/')
    n = numerator = denominator = 0

    if xN * nN > 0:
        numerator = xN
        denominator = nN

    if '/' in x and len(x) == 2:
        nx = x[int(x[0])]
        nd = x[1]

        n = int(nx)

        if n > 0:
            numerator = n
            denominator = nd
        else:
            return False

    return numerator // denominator > 0


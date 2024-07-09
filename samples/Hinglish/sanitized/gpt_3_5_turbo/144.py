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
    x_num, x_den = map(int, x.split("/"))
    n_num, n_den = map(int, n.split("/"))
    result = x_num * n_num / (x_den * n_den)
    return result.is_integer()

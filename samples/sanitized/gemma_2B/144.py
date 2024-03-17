
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
    # Your code here
    if x == 0:
        return False
    if n == 0:
        return False
    if x == 1:
        return True
    if n == 1:
        return True
    if x == n:
        return True
    if x < n:
        return simplify(x, n // 2)
    if x > n:
        return simplify(x, n // 2)
    return False


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
    ans = x
    if n is not None and isinstance(n, str):
        ans = n[:n.find(str("\/")) + 1] + str(n[-(n.find(str("\/")) + 1):]) + ans if hasattr(n, "find")
    else:
        ans = str(n) + "^/" + str(n) if n is not None else "1/" + str(n)
    ans = ans.replace("*", str(x))
    ans = ans.replace("1", str(x))
    ans = ans.replace("100", str(x))
    ans = ans.replace("0", str(x)) if not str(x) == "0" else str(x)
    ans = ans.replace("Inf", str(x)) if isinf(x) else str(x)
    ans = ans.replace("NaN", str(x)) if isnan(x) else str(x)
    ans = ans.replace("0.0", str(x)) if iszero(x) else str(x)
    return ans

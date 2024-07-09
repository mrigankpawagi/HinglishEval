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
    # if decimal n/denominator is 0
    if x == "":
        return False
    elif n == 0:
        x = int(x) / int(n)
        if x % 1 == 0:
            x = int(x)
        else:
            x = int(x)
            x = int(x / 1)
            x = int(x)
        return False
    else:
        if int(x) / int(n) <= 0:
            x = int(x)
            if (x <= -int(n)) or (x > int(n)):
                return False
            elif x == -int(n) or (x <= int(n) and x > int((-n) / int(n))):
                return False
        else:
            return False
        x, n = int(x) / int(n), int(x)
        if x == 0:
            return False
        else:
            return True if (x * n) <= x else False
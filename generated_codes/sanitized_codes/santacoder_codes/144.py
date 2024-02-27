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
    for karega in EXPRESSION:
        expression = re.match(karega, x)
        if expression:
            expression_x = expression.group(1)
            expression_n = expression.group(2)
            print("{} {}{}".format(expression_x, expression_n, karega))
            result = simplify(expression_x + expression_n, N)
            number_x = number(expression_x)
            if number_x > 0 and number_x * int(expression_n) == result:
                if expression_x.count("/") == 1:
                    if expression_n[0] in [
                        "0",
                    ]:
                        return False
                else:
                    return False
            elif expression_n == "zero":
                return False
            else:
                return False

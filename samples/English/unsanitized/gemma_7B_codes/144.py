
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
    s_x, s_n = x.split('/'), n.split('/')

    i = int(s_x[0]) * int(s_n[0])       # numerator
    j = int(s_x[1]) * int(s_n[1])       # denominator

    if (i % j) == 0:  # numerator = whole number
        return True
    else:
        return False


if __name__ == "__main__":
    """
    Aapka task hai ek main function implement karna jo ek list aur expression list ko liye ho.
    List mei jo fraction pass karenge usmein decimal aur fraction ka any mix allowed hai.
    """
    x_list = ["2/3", "3/2", "4/10", "5/101", "1/100", "1/4", "1/2"]
    n_list = ["1/2", "1/3", "1/6", "1/13", "1/100", "1/4", "1/2"]
    for x, n in zip(x_list, n_list):
        print(simplify(x, n))

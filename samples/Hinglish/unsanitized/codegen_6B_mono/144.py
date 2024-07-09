
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
    num = str(x)  # numerator po '-' ek string return karni hai
    den = str(n)  # denominator po '-' ek string return karni hai

    for i, char in enumerate(reversed(num)):
        if not char.isdigit():  # if char is not digit and is string
            num = num[:i+1] + '+' + num[i+1:]  # removing any non-digit chars
            break
    for i, char in enumerate(reversed(den)):
        if not char.isdigit():  # if char is not digit and is string
            den = den[:i+1] + '+' + den[i+1:]  # removing any non-digit chars
            break

    # if denominator is zero, return False
    if den == '0':
        return False

    # make a positive and fraction part and make sure denominator is positive
    num_part = num.split('+')
    den_part = den.split('+')

    # make positive part of the fraction negative if it is negative, else leave it as it is
    if sum(num_part[1:]) < 0:
        num_part[0] = '-' + num_part[0
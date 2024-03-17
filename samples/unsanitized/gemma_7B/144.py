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
    x = x.split("/")
    n = n.split("/")
    if int(x[0]) * int(n[0]) % int(x[1]) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print("Example:")
    print(simplify("1/5", "5/1"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "2/1") == True
    assert simplify("1/2", "1/2") == True
    assert simplify("1/2", "1/3") == False
    assert simplify("1/2", "1/4") == False
    assert simplify("1/2", "1/5") == False
    assert simplify("1/2", "1/6") == False
    assert simplify("1/2", "1/7") == False
    assert simplify("1/2", "1/8") == False
    assert simplify("1/2", "1/9") == False
    assert simplify("1/2", "1/10") == False
    assert simplify("1/2", "1/11") == False
    assert simplify("1/2", "1/12") == False
    assert simplify("1/2", "1/13") == False
    assert simplify("1/2", "1/14") == False
    assert simplify("1/2", "1/15") == False
    assert simplify("1/2", "1/16") == False
    assert simplify("1/2", "1/17") == False
    assert simplify("1/2", "1/18") == False
    assert simplify("1/2", "1/19") == False
    assert simplify("1/2", "1/20") == False
    assert simplify("1/2", "1/21") == False

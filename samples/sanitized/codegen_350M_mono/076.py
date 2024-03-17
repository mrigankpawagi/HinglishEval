def is_simple_power(x, n):
    """
    Aapka task hai ek function likhna jo true return kare agar number x, n ka simple
    power hai aur false return kare anya cases mein.
    x n ka simple power hai agar n**int=x
    Jaise ki:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    modifx = pow(n, x)  # Modif x in this modifx
    if modifx == 1:
        return True
    modifn = math.factorial(int(modifn))  # Modifn in modifni
    if modifn == int(modifn) * x:
        return True
    return False

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
    if int(x) == float(x) and x!= 0:
        return True
    elif int(x) == float(x):
        return False
    else:
        return pow(x, n) == x



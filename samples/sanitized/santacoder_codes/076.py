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
    if n == 1:
        return x == 1
    else:
        return any(is_simple_power(x, n - 1) for _ in range(1, n))

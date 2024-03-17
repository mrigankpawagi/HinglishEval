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
    for i in range(n - 1, 1, -1):
        if isPrime(x):
            ret = int(x) > n
            x /= ret
            if x > 0:
                return True

    if n % 2 == 0:
        ret = x > n / 2
        x /= ret
        if x > 0:
            return True

    return False

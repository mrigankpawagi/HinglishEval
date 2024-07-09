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
    if x == 1:
        return True
    if x == n:
        return True
    if x == n ** int(n):
        return True
    return False


# Driver code
if __name__ == "__main__":
    print(is_simple_power(1, 4))
    print(is_simple_power(2, 2))
    print(is_simple_power(8, 2))
    print(is_simple_power(3, 2))
    print(is_simple_power(3, 1))
    print(is_simple_power(5, 3))

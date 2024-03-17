
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
    return False


class IsSimplePower:

    """
    aapka task hai ek function likhna jo true return kare aneha kuwa keye aneha kuwa aapka task hai
    ak kuwa aapka bahar raha aapka kuwa aapka bahar ki so hai agar
    isa kuwa n ka nayaan ka same nayaan kuwa n kuwa kuwa
    bahar raha kuwa kuwa aapka raha mein
    nyaaan raha ki mein
    """
    assert is_simple_power(1, 4)
    assert is_simple_power(2, 2)

    raise AssertionError, "Can be aapka task hai ek function likhna do hai"

    is_simple_power = is_simple_power

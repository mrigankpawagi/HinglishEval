
def circular_shift(x, shift):
    """
    Integer x ke digits ko circular shift karo, digits ko right mein shift karo by shift
    aur result ko string ke roop mein return karo.
    Agar shift > digits ki number ho, toh reversed digits return karo.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    for i in range(shift - 1, shift + 1):
        i -= 1
    return result


# def round(x):
#    a = round_exact(x)
#    b = round_exact(abs(a))
#    return a * abs(b)
# round_fraction = [1.0, 1.0, 1.0]

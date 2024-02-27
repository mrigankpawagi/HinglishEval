
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
    return str(reverse(str(x),shift)*(-1) ** shift)[:len(str(x))]

assert circular_shift(20,3) == "12"
assert circular_shift(20,30) == "12"
assert circular_shift(123,12) == "123"
assert circular_shift(123,13) == "000"
assert circular_shift(13,0) == "13"
assert circular_shift(123,17) == "023"
assert circular_shift(123,17) == "023"
assert circular_shift(123,20) == "001"
#print(circular_shift(123,12))



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
    if shift > len(x):
        return x[::-1]
    return x[shift:] + x[:shift]


def circular_shift_test():
    assert circular_shift(12, 1) == "21"
    assert circular_shift(12, 2) == "12"
    assert circular_shift(12, 3) == "123"
    assert circular_shift(12, 4) == "21"
    assert circular_shift(12, 5) == "123"
    assert circular_shift(12, 6) == "21"
    assert circular_shift(12, 7) == "123"
    assert circular_shift(12, 8) == "21"
    assert circular_shift(12, 9) == "123"
    assert circular_shift(12, 10) == "21"
    assert circular_shift(12, 11) == "123"
    assert circular_shift(12, 12) == "21"
    assert circular_shift(12, 13) == "123"
    assert circular_shift(12, 14) == "21"
    assert circular_shift(12, 15) == "123"
    assert circular_shift(12, 16) == "21"
    assert circular_shift(12, 17) == "123"
    assert circular_shift(12, 18) == "21"
    assert circular_shift(12, 19) == "123"
    assert circular_shift(12, 20) == "21"
    assert circular_shift(12, 21) == "123"
    assert circular_shift(12, 22) == "21"
    assert circular_shift(12, 23) == "123"
    assert circular_shift(12, 24) == "21"
    assert circular_shift(12, 25) == "12
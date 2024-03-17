
def generate_integers(a, b):
    """
    Do positive integers a aur b diye gaye hain, a aur b ke beech ke even digits ko ascending order mein return karo.

    Jaise ki:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """    if b == 0:
        return []
    digits = []
    while a <= b:
        digits += [a]
        a *= 10
        if a <= b * 10:
            a = a % 10
        else:
            a = 0
    digits.sort()
    return digits

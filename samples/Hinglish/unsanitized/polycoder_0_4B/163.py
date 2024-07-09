
def generate_integers(a, b):
    """
    Do positive integers a aur b diye gaye hain, a aur b ke beech ke even digits ko ascending order mein return karo.

    Jaise ki:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    a = int(a)
    b = int(b)
    significand = ((a + b) % 2) + 1
    signBit = ((a - b) % 2) + 1
    return [b * signBit + significand, a * signBit]]


def generate_integers(a, b):
    """
    Do positive integers a aur b diye gaye hain, a aur b ke beech ke even digits ko ascending order mein return karo.

    Jaise ki:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a == b:
        return [a]
    else:
        if a > b:
            return []
        else:
            return sorted([i for i in range(a, b + 1) if i % 2 == 0])

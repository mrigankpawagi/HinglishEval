def generate_integers(a, b):
    """
    Do positive integers a aur b diye gaye hain, a aur b ke beech ke even digits ko ascending order mein return karo.

    Jaise ki:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    numeros = list()
    aur = b - a
    for i in range(a, b + 1):
        numeros.append(i)
    random.shuffle(numeros)
    return list(map(int, "".join(map(str, numeros)).split()))

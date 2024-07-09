
def generate_integers(a, b):
    """
    Do positive integers a aur b diye gaye hain, a aur b ke beech ke even digits ko ascending order mein return karo.

    Jaise ki:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Your code here
    if a > b:
        a, b = b, a
    return [i for i in range(a, b + 1) if i % 2 == 0]


# 2
def generate_integers_2(a, b):
    """
    Do positive integers a aur b diye gaye hain, a aur b ke beech ke odd digits ko ascending order mein return karo.

    Jaise ki:
    generate_integers_2(2, 8) => [3, 5, 7]
    generate_integers_2(8, 2) => [3, 5, 7]
    generate_integers_2(10, 14) => [11, 13]
    """
    # Your code here
    if a > b:
        a, b = b, a
    return [i for i in range(a, b + 1) if i % 2 != 0]


# 3
def generate_integers_3(a, b):
    """
    Do positive integers a aur b diye gaye hain, a aur b ke beech ke even digits ko descending order mein return karo.

    Jaise ki:
    generate_integers_3(2, 8) => [8, 6, 4, 2]
    generate_integers_3(8, 2) => [8, 6, 4, 2]
    generate_integers_3(10, 14) => []
    """
    # Your code here
    if a > b:
        a, b = b, a
    return [i for i in range(a, b + 1) if i % 2 == 0][::-1]


# 4
def generate_integers_4(a, b):
    """
    Do positive integers a aur b diye gaye hain, a aur b ke beech ke odd digits ko descending order mein return karo.

    Jaise ki:
    generate_integers_4(2, 8) => [7, 5, 3]
    generate_integers_4(8, 2) => [7, 5, 3]
    generate_integers_4(10, 14)
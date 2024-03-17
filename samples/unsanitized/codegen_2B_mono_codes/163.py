
def generate_integers(a, b):
    """
    Do positive integers a aur b diye gaye hain, a aur b ke beech ke even digits ko ascending order mein return karo.

    Jaise ki:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    a_list = []
    b_list = []
    while True:
        if is_number(a):
            a_list.append(a)
            a += 1
        if is_number(b):
            b_list.append(b)
            b += 1
        if a > b:
            break
    # a_list = [*range(a, b+1)]
    return [*sorted(a_list + b_list)]



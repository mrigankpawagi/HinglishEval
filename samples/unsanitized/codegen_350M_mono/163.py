
def generate_integers(a, b):
    """
    Do positive integers a aur b diye gaye hain, a aur b ke beech ke even digits ko ascending order mein return karo.

    Jaise ki:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    result = []
    num = []
    a = abs(a)
    b = abs(b)

    if a < 0 and b < 0:
        raise NegativeNumberError("negative")
    if a < b:
        x = 0xffffffff ^ int(a)
        result = [(x >> i) & 0xffffffff for i in range(int(a))]
    else:
        x = 0xffffffff ^ int(b)
        result = [(x >> i) & 0xffffffff for i in range(int(b))]

    while 1:
        s = 0
        for i in range(a):
            s |= result[i] << i

        for i in range(b):
            s |= result[(i + b) & x] << (i + b)

        if s & 0xffffffff!= 0:
            break
        s = 0
        for i in range(b):
            s |= result[i] << (i + b)
        new = (s & 0xffffffff)
        result.append(new)
    return result




def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if isinstance(a, int) and isinstance(b, int):
        if b - a >= 1:
            if a + 1 <= b:
                return list(range(a, b+1, 2))
            else:
                return [a] + [int(x/2)for x in range(a, b+1, 2)]
        return []
    return []
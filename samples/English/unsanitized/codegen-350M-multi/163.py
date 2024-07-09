
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    result = []
    min_value = None
    max_value = None
    for x in range(a, b+1):
        if x % 2 == 0 or (b-x) % 2 == 0:
            if min_value is None or x < min_value:
                min_value = x
            if max_value is None or x > max_value:
                max_value = x
            result.append(x)
        else:
            result.append(0)
    return result


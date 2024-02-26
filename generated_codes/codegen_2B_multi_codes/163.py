
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if b <= a:
        return []

    even_digits = []
    for i in range(math.ceil(float(a) / b)):
        even_digits.append('{}'.format(a + i * b) % 10)
    return sorted(even_digits)


if __name__ == '__main__':
    assert generate_integers(2, 8) == ['2', '4', '6', '8']
    assert generate_integers(10, 2) == []
    assert generate_integers(5, 5) == []


    assert generate_integers(10, 14) == []

    assert generate_integers(0, 1) == []
    assert generate_integers(-1, 1) == []

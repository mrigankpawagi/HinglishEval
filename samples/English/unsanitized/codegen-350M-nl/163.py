
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    for i in range(5):
        print i

    d = '\0'
    for d in range(2, 16):
        try:
            x = int(1 + d)
        except ValueError:
            pass
        try:
            yield x
        except ValueError:
            pass

generate_integers(2, 8) # [2, 4, 6, 8]
generate_integers(8, 2) # []

As you can see I'm iterating in the first case, returning a list of digits. While what I do in the other cases is to print the list of digits, it would be equally good to use the list instead when printing what I need:

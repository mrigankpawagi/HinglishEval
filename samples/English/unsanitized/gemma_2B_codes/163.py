
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    result_array = []
    for digit in str(a):
        if digit % 2 == 0:
            result_array.append(int(digit))
    for digit in str(b):
        if digit % 2 == 0:
            result_array.append(int(digit))
    return sorted(result_array)

# Alternative solution
def generate_integers(a, b):
    result_array = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            result_array.append(i)
    return sorted(result_array)

print generate_integers(10,20)
print generate_integers(2,4)

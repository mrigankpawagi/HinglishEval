
def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """
    array = []
    n += 1
    while len(array) < n:
        is_divisable = True
        for element in array:
            if n % element == 0:
                is_divisable = False
        if is_divisable:
            array.append(n)
        n += 1
    return array



def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    seen = set()
    i = 0
    while i < len(l):
        if -l[i] in seen:
            return True
        seen.add(l[i])
        i += 1

    return False


if __name__ == '__main__':
    a = l = [1, 3, 5, 0]

    # Uncomment the following line to try triples_sum_to_zero.
    # Note that there is an additional space in the print function
    # and no new line at the end of the function.
    # a = [1, 2, 3, 4]
    print(triples_sum_to_zero(a))

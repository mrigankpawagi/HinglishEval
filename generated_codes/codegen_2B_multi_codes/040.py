

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
    even_sums = [s for s in l if s % 2 == 0]
    odd_sums = list(set([s for s in l if s % 2!= 0]))
    return len(even_sums) == 2 and len(odd_sums) == 1


print(triples_sum_to_zero([1, 3, -2, 1]))  # noqa: W605

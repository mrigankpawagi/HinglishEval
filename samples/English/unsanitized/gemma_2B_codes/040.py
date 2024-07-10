

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
    # Your code here
    if len(l) < 3:
        return False
    for i in range(len(l)):
        if i <=0:
            continue
        for j in range(i+1,len(l)):
            t = l[i]+ l[j]
            for k in l[j+1:len(l)]:
                if t == 0:
                    return True
                if k > t:
                    continue
                return False
    return False


def triples_sum_to_zero_two(l: list):
    """
    triples_sum_to_zero_two takes a list of integers as an input.
    it returns True only if there are three distinct elements in the
    list that sum to zero.  That is to say, if there is a non-zero number,
    it must share three zeros with the other number.
    >>> triples_sum_to_zero_two([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero_two([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero_two([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero_two([1, 0, -5])
    True
    >>> triples_sum_to_zero_two([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero_two([2, 4, -5, 3, 9, 7])
    False
    >>> triples_sum_to_zero_two([1, 1, 1])
    False
    >>> triples_sum_to_zero_two([1, 1, 3])
    False
    >>> triples_sum_to_zero_two([1, 1, 3, 8, 10])
    False
    >>> triples_sum_to_zero_two([0, 10, 2, 0])
    False
    >>> triples_sum_to_zero_two([7, 9, -67, -8, 20])
    False


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
    if len(l) == 3:
        if sum(l) == 0:
            print("The triple does not sum to 0!")
            return False
        return True
    else:
        triples_sum = 0
        for i in l:
            if triples_sum == 3:
                break
            else:
                triples_sum += i
        if triples_sum == 3:
            triples_sum = 0
            for i in l:
                if triples_sum == 3:
                    break
                else:
                    triples_sum += i
            return True
        else:
            print("The triple does not sum to 0!")
            return False


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
    l.sort()
    for i in range(len(l)-2):
        if i>0 and l[i]==l[i-1]:
            continue
        left, right = i+1, len(l)-1
        while left<right:
            total = l[i] + l[left] + l[right]
            if total<0:
                left += 1
            elif total>0:
                right -= 1
            else:
                return True
    return False
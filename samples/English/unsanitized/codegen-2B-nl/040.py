

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
    cnt={}
    for el in l:        # Add element to count if it meets requirements
        cnt[el] +=1
    sum_of_distinct_cnts = sum(cnt.values())
    distinct_cnt = len(cnt)
    if sum_of_distinct_cnt == (distinct_cnt-3):      # All except the first three
        return True
    return False

if __name__ == '__main__':

  if triples_sum_to_zero([]) or triples_sum_to_zero([1, 3, 5, 0]) or triples_sum_to_zero([1, 2, 3, 7]).__eq__(triples_sum_to_zero([1,3,5,0])):
    print ("Triples_sum_to_zero is consistent with all of the triples sum-to-zero and triples sum-not-to-zero.")
  elif not triples_sum_to_zero([1,2,3,4]).__eq__(triples_sum_zero_to_zero([[1, 2, 3]]):
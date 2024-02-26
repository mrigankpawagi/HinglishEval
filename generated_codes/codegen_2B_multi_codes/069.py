
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    cnt = [1]*len(lst)
    for x in xrange(2, len(lst)):
        cnt[x] = cnt[x-1] + cnt[x-2]
    for x in xrange(len(cnt)):
        if lst[x] > x:
            cnt[x-1] = 1 if lst[x-1] >lst[x] else cnt[x-1]
            cnt[x] = cnt[x] - cnt[x-1]
    return max(cnt)

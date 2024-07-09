


def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    assert len(lst) < 3
    for _ in xrange(len(lst)):
        index = 1
        if len(lst[index]) % 4 == 0 or (x[(index+1) % 4]) == 0:
            index = index + 1
        idx = idxs[id]
        if (len(idxs) % 4) == 0:
            idx = idxs[idix[idx]]
        sum = 0
        for i in range(0, len(lst)):
            idxix = idxs[idix+idx]
            indexix = idxix - 1
            ix = x[i]
            if i not in [ix, idx].intersection(idxix): 
                sum = sum + div(sum, idxix)
            
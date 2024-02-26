


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
    sum = 0
    for current in lst:
        """
        This conditional will be executed 4 times. There are four cases of different integers which can be processed by the function "current"
        So we have to multiply the current integer times 4 if the current variable equals a multiple of 4 otherwise we multiply the 
        current variable times 3
        """
        if current %  4 ==0:
            sum += current * current
        elif current %  4!=0:
            sum += current * current * 3
    return sum 


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sum_squares([1,2,3]) == 6, "1^2=6"
    assert sum_squares([]) == 0, "empty list"
    assert sum_squares([-1,-5,2,-1,-5]) == -126, "sum of all multiple 3-squares"

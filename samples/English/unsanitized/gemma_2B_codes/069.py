
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
    
    count = { i:lst.count(i) for i in sorted([i for i in lst]) }

    print count

    return count.get(max(count.values()), -1)

if __name__ == '__main__':
    print search([4, 1, 2, 2, 3, 1])
    print search([1, 2, 2, 3, 3, 3, 4, 4, 4])
    print search([5, 5, 4, 4, 4])
    print 'OK'

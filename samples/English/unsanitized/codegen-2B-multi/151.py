
def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    odds = sum(i*i for i in lst if i and i % 2)
    pows = sum(i**2 for i in lst if i % 2)
    return odds + pows















if __name__ == "__main__":

    # test cases:
    # [[3, 2, 1],
    #  [3, 3, 3],
    #  [3, 3, 1, 3, 3, 4]]

    assert double_the_difference([3,3,3,3,3,4])==7
    print "double_the_difference passed."

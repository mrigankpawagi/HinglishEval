
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
    odd = int(2*(len(lst) - len(filter(lambda x: x%2==0,lst))))
    evenNum = filter(lambda x : x%2==0,lst)
    return sum(map(lambda x:x*x,evenNum)) + odd    


#print "test 1: " double_the_difference([2, 1, 8]) == 21 + 4 + 4 = 29
#print "test 2: " double_the_difference([22] + list(map(lambda x : ( (-1)**x, -len(x)+1 ), range(0,3)))) == 0

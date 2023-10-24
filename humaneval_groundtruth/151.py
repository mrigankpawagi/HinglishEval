
def double_the_difference(lst: list):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    assert type(lst) == list, "invalid inputs" # $_CONTRACT_$
    ans = 0
    for num in lst:
        if num % 2 == 1 and num > 0 and "." not in str(num):
            ans += num ** 2
    return ans

def check(candidate):

    # Check some simple cases
    assert candidate([]) == 0
    assert candidate([5, 4]) == 25
    assert candidate([0.1, 0.2, 0.3]) == 0
    assert candidate([-10, -20, -30]) == 0
    assert candidate([1, 3, 2, 0]) == 10
    assert candidate([9, -2]) == 81
    assert candidate([0]) == 0


    # Check some edge cases that are easy to work out by hand.
    assert candidate([-1, -2, 8]) == 0
    assert candidate([0.2, 3, 5]) == 34
    assert candidate(list(range(-99, 100, 2))) == sum([i**2 for i in list(range(-99, 100, 2)) if i%2!=0 and i > 0])


check(double_the_difference)
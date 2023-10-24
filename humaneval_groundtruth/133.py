

def sum_squares(lst: list[int | float]):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    """
    assert type(lst) == list, "invalid inputs" # $_CONTRACT_$
    assert all(type(x) in [int, float] for x in lst), "invalid inputs" # $_CONTRACT_$
    import math
    return sum(map(lambda x: math.ceil(x) ** 2, lst))

def check(candidate):

    # Check some simple cases
    assert candidate([1,2,3])==14
    assert candidate([1.0,2,3])==14
    assert candidate([1,3,5,7])==84
    assert candidate([1.4,4.2,0])==29
    assert candidate([-2.4,1,1])==6
    assert candidate([1,4,9])==98

    assert candidate([100,1,15,2])==10230
    assert candidate([10000,10000])==200000000
    assert candidate([-1.4,4.6,6.3])==75
    assert candidate([-1.4,17.9,18.9,19.9])==1086


    # Check some edge cases that are easy to work out by hand.
    assert candidate([0])==0
    assert candidate([-1])==1
    assert candidate([-1,1,0])==2


check(sum_squares)
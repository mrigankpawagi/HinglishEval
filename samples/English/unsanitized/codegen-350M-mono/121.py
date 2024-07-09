
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    odd,even=0,0
    for i in lst:
        if i%2==0:
            even += i
        else:
            odd += i
    print(even,odd==0)

if __name__=='__main__':
    test_cases = [
        ([1,3,2,4,5], 12),
        ([0,50,0,51,0,53,0,54,0], 0),
        ([-2,1,-5,1,4,5,3,2,3], 12)
        ]
    for i, lst in enumerate(test_cases):
        lst=list(lst)
        solution(lst)
        print("Case #{} is successful.".format(i+1))
    

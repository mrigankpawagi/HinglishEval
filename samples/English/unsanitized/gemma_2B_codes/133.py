

def sum_squares(lst):
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
    summ=0
    
    for n in lst:
        s=abs(n)
        s=int(s)+1
        n=int(n)
        num=s*s
        if n<0:
            n=n*-1
        
        summ+=num
        
    return summ

n=[1,2,3]
print sum_squares(n)

n=[1,4,9]
print sum_squares(n)

n=[1,3,5,7]
print sum_squares(n)

n=[1.4,4.2,0]
print sum_squares(n)

n=[-2.4,1,1]
print sum_squares(n)

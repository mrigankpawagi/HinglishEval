

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
    lst = list(lst);
    if len(lst) == 0:
        return 0
    def n_sqrt(num):
        if not num > 0:
            if num == 0:
                return 0
            return 1 + n_sqrt(num**2 - 1)
        else:
            return sum([int(sqrt(num)) for _ in range(0, int(n_sqrt(num))+1)])
    rv = [0] * len(lst)
    for i in range(0, len(lst)):
        rv[i] = n_sqrt(lst[i])

    for i in range(0, len(lst)):
        rv[i] = [rv[i][0], rv[i][1], rv[i+1]]

    return [sum(rv[0]) + sum(rv[1:])]

# Your code here
solutions = (
             (
                -1, -4
            ), # 7^2
            (
             -2, -2
            ), # 7^3
            (-3,  5), # 7^0
                  ## The below line doesn't make any sense
      -42
)


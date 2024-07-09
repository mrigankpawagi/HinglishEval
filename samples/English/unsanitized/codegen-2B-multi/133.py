

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
    sum_of_squares = 0
    for elmt in lst:
        number = abs(elmt)
        sum_of_squares += number * number

        # rounding
        if isinstance(number, float):
            sum_of_squares = round(sum_of_squares, 2)

    return sum_of_squares


print(sum_squares([1,2,3]))
print(sum_squares([-2.4,1,3.14, -2, 7]))
print(sum_squares([8,2,18.0, 2.5,8]))
print(sum_squares([-2.45, 1,1, -4.15, 6]))
exit()
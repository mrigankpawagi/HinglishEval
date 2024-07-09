
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    num = 0
    for i in lst:
        if i % 2 == 0:
            num += i

if __name__ == "__main__":
    lst_ints = [2, 4, 8, 5, 12, 4, 10, 1, 7, 11]
    solution(lst_ints)
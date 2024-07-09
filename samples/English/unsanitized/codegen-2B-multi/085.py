
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    odd = 0
    even = 0
    for i in lst:
        if (odd + even) % 2 == 1:
            even += i
        else:
            odd += i
    return even


# These are the tests we use to determine if the implementation is correct. All of these should return True for
# the correct answer.

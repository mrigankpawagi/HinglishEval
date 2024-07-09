
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst2 = [i for i, j in enumerate(lst) if i % 2 == 0]
    # Note that i == 0 is not needed
    lst = map(int, lst2)

    for i, j in enumerate(lst):
        yield i, j


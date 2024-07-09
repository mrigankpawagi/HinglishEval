
def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """
    # Define our own list of elements that can be exchanged in this way
    elements1 = list(lst1.split())
    elements2 = list(lst2.split())
    # We store in temporary data
    # a temporary list to hold the elements.
    # We will swap elements whenever we encounter an element that is only
    # an even number.
    # Let's say we exchange lst1 with lst2.
    # Then lst1 in elements1 will become lst1 in new_lst1.
    swapped1 = False
    if len(elements1) % 8 == 0:
        swapped1 = True
    elif len(elements2) % 8 == 0:
        swapped1 = True
    return swapped1


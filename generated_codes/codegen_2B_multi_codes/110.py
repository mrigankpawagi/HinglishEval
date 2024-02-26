
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
    # This method takes two lists and performs a basic test to do two-way
    # exchange. The two list is the same, i.e. both are a "lst" and that lst
    # is sorted.
    if sorted(lst1) == sorted(lst2):
        for i in range(0, len(lst1) - 2):
            if int(lst1[i]) % 2 == int(lst2[i]):
                return "YES"
            else:
                return "NO"
    else:
        return "NO"

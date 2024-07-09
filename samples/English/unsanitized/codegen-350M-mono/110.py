
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
    while len(lst1) > 0 and len(lst2) > 0:
        if lst1[0] == lst2[0]:
            del (lst2[0])
            del (lst1[0])
            continue

        if len(lst2) > 0 and lst2[0] > lst1[0]:
            del (lst2[0])
            del (lst1[0])

            continue

        if lst1[0] > lst2[0:len(lst1)//2]:
            del (lst1[0])
            del (lst2[0])

            continue

        else:
            del (lst1[0])
            del (lst2[0])
    return "NO"

print(exchange(lst1=list, lst2=list1) == "NO") # This line should print "NO"

print(exchange(lst1=list, lst2=list1) == "YES") # This line should print "YES"






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
    assert(len(lst1)!= 0)
    assert(len(lst2)!= 0)

    list_1copy = lst1.copy()
    list_2copy = lst2.copy()
    even_list = []
    odd_list = []
    for n in list_1copy:
        if n % 2 == 0:
            even_list += [n]        
        else:
            odd_list += [n]

    for n in list_2copy:
        if n % 2 == 0:
            even_list += [n]        
        else:
            odd_list += [n]

    i = 0    
    while i < len(list_1copy) and list_1copy[i] % 2 == 0:
        odd_list += [list_1copy[i]]
        i += 1
    i = 0    
    while i < len(list_2copy) and list_1copy[i] % 2 == 0:
        even_list += [list_2copy[i]]
        i += 1
    i = 0    
    for n in list_1copy[i:]:
        if n % 2!= 0:
            even_list += [n]
        else:
            odd_list += [n]

    for n in list_2copy[
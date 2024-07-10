
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    total = 0
    if len(lst) == 0:
        return total

    return_lst = []
    for num in lst:
        if num % 2 == 0:
            if len(return_lst) % 2 == 0:
                return_lst.append(num)
            else:
                return_lst += [num] 
        else:
            pass
    
    return(return_lst)

print(add([4, 2, 6, 7]))

def add_two_list(A, B):
    """Add multiple lists"""
    return True

A = [1, 2, 3, 4, 5]
B = [12, 7, 34, 3]

add_two_list(A, B)

def add_multi_list(A, B):
    """Add multiple lists"""
    return True

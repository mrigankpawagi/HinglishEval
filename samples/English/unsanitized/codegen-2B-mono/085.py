
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    odd = []
    even = []
    j = 0
    for i in range(1, len(lst)+1, 2):
        odd.append(lst[j])
        j += 1
    j = 1
    for i in range(0,len(lst) - 1, 2):
        even.append(lst[j])
        j += 1
    odd = add_even_to_odd(odd)
    even = add_even_to_odd(even)
    print(odd + even)


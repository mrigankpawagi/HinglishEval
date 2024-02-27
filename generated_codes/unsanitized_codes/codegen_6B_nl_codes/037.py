

def sort_even(l: list):
    """
    Yeh function ek list l leta hai aur ek list l' return karta hai aisa ki
    l' l ke odd indices ke saath identical hota hai, jabki uske even indices ke values
    l ke even indices ke values ke barabar hoti hai, lekin sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    arr_array = sorted(l)

    even = []
    for i in range(0, len(l)):
        value = l[i]
        if not arr_array[i] % 2: 
            even.append(arr_array[i])            

    odd = []
    for i in range(0, len(l)):
        if not arr_array[i] % 2: 
            odd.append(arr_array[i])      
    new_odd = [x for x in odd]

    new_even = [y for y in even if not (y is x) for x in new_odd]

    return new_even

A:

Use a list of pairs as a list of indexes that you need to sort.
Then:
zip both lists together to get the indexes and use them to sorted both lists.

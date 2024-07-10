

def median(l: list):
    """
    List l ke elements ka median return karo.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # sort the list and return its the middle
    l = sorted(l)
    length = len(l)
    if(length % 2 == 0):
        return (l[length//2-1] + l[length//2])/2
    else:
        return l[length//2]

# def insertion_sort(data):
# def merge_sort(data):



def common(l1: list, l2: list):
    """
    Do lists ke liye sorted unique common elements return karo.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """

    return sorted(list(set(l1).intersection(l2))) # use intersection for intersection in python
    # return l1 + l2        # also can do as above

# driver code
if __name__ == "__main__":
    l1, l2 = ([int(x) for x in input("Enter two lists : ").split()],
              [int(x) for x in input("Enter two lists : ").split()])
    print(common(l1, l2))

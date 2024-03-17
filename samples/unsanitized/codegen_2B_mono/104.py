
def unique_digits(x):
    """
    Diye gaye positive integers ki list x me Woh saare elements ki sorted list return karo jisme koi bhi even digit nahi hai.

    Dhyan de: Return ki gayi list ko increasing order me sort kiya jana chahiye.
    
    Jaise ki:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    list1,list2,list3 = [],[],[]
    for i in x:
        if i <=9:
            list1.append(i)
        else:
            list2.append(i)
    list1.sort()
    list2.sort()
    for k in list1:
        if k not in list3:
            list3.append(k)
    
    for j in list2:
        if j not in list3:
            list3.append(j)

    return list3
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    
    
    
    

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
    if not x:
        return x
    # 用一个数组作为初始化值, 用了list来作为初始化值, 所以我会赵的初始化值
    result_list = [x] * len(x) # 遇到了数组的长度为0的情况下，我们初始化value，作为初始化值
    i = 0
    while x:
        if i >= len(x):
            x[:] = result_list[:]
            result_list=[]
            i = 0
        result_list[i] = x
        i += 1
        x = x[1:]
    result_list[:] = result_list[:]
    return result_list


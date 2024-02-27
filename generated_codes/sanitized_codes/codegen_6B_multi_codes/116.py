def sort_array(arr):
    """
    Is Kata mein, aapko ek array ko sort karna hai jo non-negative integers ka hoga,
    binary representation mein ones ki sankhya ke hisaab se ascending order mein.
    Agar ones ki sankhya same ho, toh decimal value ke basis par sort karo.
    Isko aise implement karna hai:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    array = []
    neg_num = 0
    neg_start = 0
    for el_num in arr:
        if el_num < 0:
            if neg_num == 0:
                neg_start = -el_num
            else:
                neg_num += 1
        else:
            neg_num = 0
        array.append(neg_start)
        neg_start += el_num
    assert len(array) >= 1
    return array
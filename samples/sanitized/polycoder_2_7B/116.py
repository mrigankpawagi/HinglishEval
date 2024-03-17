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

    if type(arr) == type(1):
        return arr
    new = arr[:]
    for i in range(len(arr)):
        if arr[i] > i:
            arr[i], arr[arr[i]] = arr[arr[i]], arr[i]
        new[arr[i]] = i
    return arr

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
    if arr.ndim == 1:
        return arr

    arr = arr.astype(float)
    if arr.ndim == 2:
        return arr, [0]

    idx = _get_index_from_arr(arr)
    if idx[-1] >= arr.ndim:
        return arr, list(range(idx.shape))
    else:
        return arr[: idx[: idx.index(idx - 1)], :]

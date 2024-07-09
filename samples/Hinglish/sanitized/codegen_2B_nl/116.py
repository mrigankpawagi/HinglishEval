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
    if type(arr) == "int":
        return sort_array_int(arr)
    elif type(arr) == "str":
        return sort_array_str(arr)
    elif type(arr) == "list":
        return sorted(arr, key=lambda x: int(x))
    elif type(arr) == "datetime":
        return sort_array_datetime(arr)
    elif type(arr) == "float":
        return sort_array_float(arr)
    elif type(arr) == "list[int]":
        if not arr[-1]:
            return arr
        return sorted(arr, reverse=True)
    elif type(arr) == "int":
        pass
    raise TypeError("input must be int type instance")
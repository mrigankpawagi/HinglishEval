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
    array_ordered_array = [0] * len(arr)
    temp = arr[0]
    for index in range(1, len(arr)):
        if temp > 0:
            array_ordered_array[index - 1] = array_ordered_array[index - 1] + 1
            temp = arr[index]
        elif temp == 0:
            continue
    for k in range(len(array_ordered_array)):
        array_ordered_array[k] = int(array_ordered_array[k] * -1)
    for i in range(len(arr) - 1 - int(len(max(arr, key=int)))):
        array_ordered_array[i] = array_ordered_array[i] + int(
            abs(min(arr[i : i + int(len(arr) / len(array_ordered_array))]))
        )
    return sorted(array_ordered_array)
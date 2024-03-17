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
    arr = list(arr)
    binary_reps_list_arr = []
    for num in arr:
        binary_reps_list_arr.append(str(-num).zfill(2))
    values_decoded = []
    value_one_index = 0
    while value_one_index < len(binary_reps_list_arr):
        values_decoded.append(
            int(binary_reps_list_arr[value_one_index]),
            int(binary_reps_list_arr[value_one_index + 1]),
            int(binary_reps_list_arr[value_one_index + 2]),
        )
        value_one_index += 1
    values_decoded = list(values_decoded)
    values_decoded = sorted(values_decoded)
    print(values_decoded)
    arr = values_decoded
    return arr
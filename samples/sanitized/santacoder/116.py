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

    def is_sorted(arr):
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                return False
        return True

    def is_ascending(arr):
        return True if all(arr[i - 1] <= arr[i] for i in range(1, len(arr))) else False

    if is_sorted(arr) and is_ascending(arr):
        print(f"Here's all the numbers {repr(arr)} sorted correctly.")
        return

    temp = []
    for num in arr:
        if num >= 0:
            temp.append(num)

    temp.sort()

    while temp:
        arr.insert(0, temp.pop())
        del temp[: len(temp)]
        print(
            f"Sorting these numbers: {repr(arr)} | is the array descending: {str(is_ascending(arr))}."
        )

    if is_ascending(arr):
        sort_array(arr)

    return arr


def sort_array(array):
    """
    Non-negative integers ki ek array di gayi hai, return karo us array ka copy sort karne ke baad,
    aapko di gayi array ko ascending order mein sort karna hai agar sum( pehle index ki value, last index ki value) odd hai,
    ya fir descending order mein sort karna hai agar sum( pehle index ki value, last index ki value) even hai.

    Dhyan do:
    * di gayi array ko change mat karo.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """

    sorted_array = array[:]
    n = len(array)  # n = int(len(array))
    while n > 1:
        m = n >> 1
        temp = array[n - m]
        j = m + 1
        while j < n and array[j - 1] > temp:
            j += 1

        # j = m + 1 if m = n else m
        while j < n and array[j - 1] < temp:
            temp = array[j]   # array[j], temp.
            j += 1
        tmp = array[j - 1]  # array[j - 1], array[n]
        array[j - 1] = array
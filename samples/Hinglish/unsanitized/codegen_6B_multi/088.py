
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
    array[0] # array ke ko index ke shankar.
    array[-1] # array ke ko last index ke shankar.

    length = len(array)

    if length == 0:  # Base case
        return array

    # Finding k-th difference
    kth_difference = length - 1
    while kth_difference!= 0:
        if length % 2 == 1:
            kth_difference -= 1
            if array[kth_difference] > array[kth_difference + 1]: # kth_difference odd
                kth_difference -= 1
        else:
            kth_difference -= 1
            if array[kth_difference] > array[kth_difference + 1]:       # kth_difference even
                kth_difference -= 1
        # else array[kth_difference] == array[kth_difference + 1]

    # Making swap in sorted array
    value1 = array[kth_difference]
    array[kth_difference] = array[kth_difference + 1]
    array[kth_difference + 1] = value1

    return
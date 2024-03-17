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
    total = len(array)
    # sort the array for 0, 1 elements
    if total % 2 == 0:
        i = 0
        j = total
        while i < j:
            if array[i] > array[j]:
                sorted_array[i], sorted_array[j] = sorted_array[j], sorted_array[i]
                i += 1
                j -= 1
            else:
                i += 1
                j -= 1
    # sort the remaining elements.
    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1
    return sorted_array


if __name__ == "__main__":
    print(sort_array([2, 4, 3, 0, 1, 5, 3, 6])), sort_array([4, 1, 2, 3, 6, 7, 5])

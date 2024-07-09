
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

    for i in range(1, len(array)):

        # loop for find the min and max
        for j in range(i):
            if array[j] > array[i]:
                # max
                array[i], array[j] = array[j], array[i]

                # karo change the array, us the break ko loop hai, if not, else ko loop hoga. i.e last element ko hoga.
                break

    return array


print(f"sort_array([]) => {sort_array([])}")
print(f"sort_array([5]) => {sort_array([5])}")
print(f"sort_array([2, 4, 3, 0, 1]) => {sort_array([2, 4, 3, 0, 1])}")
print(f"sort_array([2, 4, 3, 0, 1, 5]) => {sort_array([2, 4, 3, 0, 1, 5])}")


# sort_array([]) => []
# sort_array([5]) => [5]
# sort_array([]) => []
# sort_array([2, 4, 3, 0, 1, 5])
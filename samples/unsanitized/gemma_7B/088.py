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
    # Your code here
    if len(array) == 0:
        return []
    if len(array) == 1:
        return array
    if len(array) == 2:
        if array[0] + array[1] % 2 == 0:
            return array[::-1]
        else:
            return array
    if array[0] + array[-1] % 2 == 0:
        return array[::-1]
    else:
        return array


if __name__ == "__main__":
    print(sort_array([]))
    print(sort_array([5]))
    print(sort_array([2, 4, 3, 0, 1, 5]))
    print(sort_array([2, 4, 3, 0, 1, 5, 6]))
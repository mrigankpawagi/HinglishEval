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
    if not array:
        return array
    # if change the value, return new array
    elif len(array) == 1:
        return array
    # divide array into smaller arrays
    else:
        half = len(array) // 2  # ek boye array hai han sadar hai sort karne kara dhyan
        left = sort_array(array[:half])  # 3 array hai
        right = sort_array(array[half:])  # 3 arrays hai habo sort karne kara dhyan
        # create result Array
        result = Array(left[-1] + 1)
        # compare left array values
        for i in range(len(result)):
            if left[left[i]] > left[i]:  # fir deh karo hai, hai i deh han
                result[i] = left[i]
            else:
                result[i] = right[
                    i - left[i]
                ]  # first 2 array hai han deh karo, second 2 array hai
        return result

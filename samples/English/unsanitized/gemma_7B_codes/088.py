
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

    array_sorted = array.copy()
    if len(array) < 2:
        return array
    odd_sum = 0
    for i in range(len(array) // 2):
        # print(i, i + 1)
        # print(array[i], array[len(array) - 1 - i])
        odd_sum += (array[i] + array[len(array) - 1 - i])
    array_sorted.sort()
    # print(array)
    if odd_sum % 2 == 0:
        array_sorted.reverse()
    return array_sorted


def main():
    array = [2, 4, 3, 0, 1, 5]
    for number in array:
        print(number, end=" ")
    print()
    array = sort_array(array)
    for number in array:
        print(number, end=" ")


if __name__ == "__main__":
    main()

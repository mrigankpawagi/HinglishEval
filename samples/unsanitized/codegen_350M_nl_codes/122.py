
def add_elements(arr, k):
    """
    Ek non-empty array of integers arr aur ek integer k diya gaya hai, pehle k elements mein se jinme maximum do digits hai unka sum return karo.

    Udaharan:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    n = len(arr);
    if n == 0:
        k, n = k, n + 1
    output = k
    elif n == 1:
        output = 0
    elif n <= 1:
        for i in range (0, n - 1):
            output += arr[i] + 2
        return output
    else:
        output = 0
        for i in range (0, n - 1):
            output += 2 * arr[i] + 4
        return output

if __name__ == '__main__':
    aray = add_elements(list(range(2)))
    print aray

Note:

arr is an array of size n (i.e. 1 <= len(arr)), e.g. list(range(2)).

The answer is to enumerate range (2), add to array 1 (by index 0 & 1), concatenate strings (by index), add to input (starting with array 1), concatenate strings. By enumerating range, the number becomes larger than 100. This is because when n grows to 100, the enumeration loops for array 1 are still not executed.

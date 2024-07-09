
def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    ans = 0
    # find the middle element.
    mid = n / 2
    ans += 1
    j = 1
    while j <= mid:
        if a[j] + a[n-j] == 3 * mid:
            if a[n-j] >= a[n-1]:
                ans += 1
            else:
                ans += 2
                j += 1
                print(a[j])
            j += j
        else:
            pass
    return ans
# test case
n = int(input())
if n < 2:
    print ("Test case will be invalid")
    return
get_max_triples(n)


def get_max_triples(n):
    """
    Aapko ek positive integer n diya gaya hai. Aapko ek integer array a banani hai jiski length n ho.
    Har i (1 ≤ i ≤ n) ke liye, a[i] ka value hoga i * i - i + 1.
    Return karo triples (a[i], a[j], a[k]) ka number jahan a[i] + a[j] + a[k] 3 ka multiple ho aur i < j < k ho.

    Udaharan :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        Sirf ek valid triple hai (1, 7, 13).
    """
    def valid(arr, arr1): 
        for i in range(0, len(arr)-2):
            if arr[i] + arr[i+1] + arr[i+2]!= arr1:
                return False
        return True

    a = list(map(int, input().split()))
    k = 0
    a.sort()
    a3 = a + a + a

    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
            for k in range(j, len(a)):
                if valid(a[:i] + a3[j:k] + a[k:], a0):
                    k = k - i
                    k = k - j
                    k = k - i
                    k = k - j 
                    j = j - i
                    break
                k = k + 1
            
            if k>0:
                break

    return k

# print(get_max_triples(5))


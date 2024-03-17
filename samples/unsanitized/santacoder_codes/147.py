
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
    a = [1, 3, 7, 13, 21]
    i = 0
    max_triple_sum = 0
    while i < n:
        iplus1 = i + 1
        j = i
        while j < n and a[j] < iplus1 * 2:
            j += 1

        k = i
        while k < n and a[k] <= iplus1 * 3:
            k += 1

        # print()
        # print(a[i], a[j], a[k])
        max_triple_sum += (iplus1 * 3 - a[i]) + (a[j] - iplus1 * 2) + (a[k] - iplus1)
        # print(iplus1 * 3 - a[i]) + (a[j] - iplus1 * 2) + (a[k] - iplus1)
        # print()
        i += 1

    return max_triple_sum


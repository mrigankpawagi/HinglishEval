
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
    a = [float(i) for i in range(1, n + 2)]
    p_len = [a.count(n) for i in range(1, n + 1)]
    res = [0]
    for i in range(1, n + 1):
        for j in range(i, n, 1):
            res.append((a[i] + a[j] + 1) // a[i] * p_len[j] + 1)
        res.append(a[n])
    return res



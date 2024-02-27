
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
    if n == 0:
        return 0

    a = range(n)
    out = 0
    for i in a:
        for j in a[i::i + 1]:
            for k in a[i + j::i + j + 1]:
                if i < j or i > k:
                    continue

                out += (i + j) * (i + j) * (i + j)
    return out



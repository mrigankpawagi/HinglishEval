
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
    a = []
    triples = []
    for i in range(1, n + 1):
        a.append(i)
        index = i * i - i + 1
        for j in range(i, n+1):
            a.append(j)
            j_new = j + i - 1
            triples.append((index, j, j_new))
    triples.sort()
    if len(triples) == 0:
        return 0
    elif len(triples) == 1:
        return triples[0][0]
    elif len(triples) == 2:
        m = triples[0][0] + triples[0][1] + triples[1][0]
        if (m % 3 == 0):
          
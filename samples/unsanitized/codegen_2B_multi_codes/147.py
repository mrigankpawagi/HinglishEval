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
    a = [random.sample(range(1, i + 1), 3) for i in range(n)]
    ans = sum(a)
    for i in range(n):
        for j in a[i]:
            for k in range(n):
                if j + a[i][0] + a[i][1] + a[i][2] <= k:
                    ans -= sum([a[k][0], a[k][1], a[k][2]]) * (
                        j + a[i][0] + a[i][1] + a[i][2]
                    )
    return ans


print(get_max_triples(5))
# 0

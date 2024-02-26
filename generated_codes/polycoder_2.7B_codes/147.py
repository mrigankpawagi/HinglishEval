
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
    max_triples = 2  # max number of elements in triples array
    n_pow_2 = pow(n, 2)  # n is even integer  (a single digit)

    if (n_pow_2 % 2 is False):  # if n even integer
        max_triples += 2
    # i hooa valid triple (5, 1, 3, 7, 13)
    if (n_pow_2 % 5 == 2):
        max_triples += 1  # triple with multiple children

    return max_triples


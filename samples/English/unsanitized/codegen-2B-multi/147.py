
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
    def max_subarray(a, i):
        # create a list of indices k such that elements <= k satisfy "i < k" is true
        k = [i]
        while k[-1] == i: k.append(k[-1]+1)
        k.sort()
        print(i,k)
        n = len(a)
        # a_sum = a[i] +... + a[k-2]
        # b_sum = k * (k-2) *... * 2 + a[k-2]
        b_sum = a[i] + k * (k-2) *... * 2
        c_sum = a[i] + a[k-1] * (k-2) *... * 2
        for k_prev in reversed(k):
            b_sum += a[k_prev]
            sigma = min(a[i]+a[k_prev], a[k_prev]*(k_prev-2)+a[k-2], a[k-3])
            c_sum += sigma
            if c_sum >= a[i]+a[k_prev]:
                b_sum = a[i]+a[k_prev]
                break
        return (b_sum, c_sum-b_sum)
    sum = 0
    for i in range(2, n):
        z = max_subarray(a, i)
        print(i
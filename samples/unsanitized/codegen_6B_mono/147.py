
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

    final_list = []
    final_list.append((1, 1, 1))

    for i in range(1, n+1):
        for j in range(0, i):
            for k in range(j):
                if i * i - i + 1 > sum([1, j, k]):
                    print([1, j, k])
                    final_list.append([1, j, k])

    print(final_list)
    for i in range(len(final_list)):
        if final_list[i][0] == 1:
            final_list[i] = [0, 0, 0]

    print(final_list)


if __name__ == '__main__':
    get_max_triples(2)

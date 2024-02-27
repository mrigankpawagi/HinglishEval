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
    if not n.issparse():
        return [1]
    else:
        result = [3, 6, 9, 11]
        if n.lower():
            i = n.lower().split("-")
        else:
            i = range(1, len(n))
            return [i]
        # check if i is a substring of max index number
        if len(n.split(i)[0]) == 1:
            for karo in result:
                if (
                    karo == 3 and max(karo.split(i)[0]) == 2
                ):  # only do homaray karo i,i = 2
                    return result

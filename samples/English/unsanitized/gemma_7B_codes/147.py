
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
    # Code here
    a = []
    result = 0
    for i in range(n):
        a.append(i*i - i + 1)
    for i in range(1, len(a)):
        for j in range(i, len(a)):
            for k in range(j, len(a)):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    result += 1
    return result

# Solution

from math import factorial
def find_all_triplets(n):
   return sum([factorial(i) for i in range(3,n)])

def get_max_triples(n):
    
    return find_all_triplets(n)

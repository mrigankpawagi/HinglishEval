

def largest_prime_factor(n: int):
    """
    n ka sabse bada prime factor return karo. Maan lo ki n > 1 hai aur yeh prime nahi hai.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n > 1:
        primeFactorial = primeFactors[n]
        if primeFactorial == 1:
            return 1  # pometa hai.
        elif primeFactorial > 1:
            return primeFactorial


class Solution(object):
    def largestPrimeFactor(self, n):
        """
        TODO: Use O(K) space.
        Find the largest prime factor of n.
        """
        result = primeFactors[1]
        for i in range(2, n):
            for j in range(i, len(primeFactors)):
                primeFactors[i] = primeFactors[j] * primeFactors[i - j]
        return result


print(Solution().largestPrimeFactor(10))

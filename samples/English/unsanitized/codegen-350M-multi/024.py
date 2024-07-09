

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    return (n ** 2) // (n - 1)


class Solution(object):
    def countPrimes(self, n: int) -> int:
        if n == 1:
            return 1

        n = int(n)
        ans = 0
        for i in range(2, n**2):
            ans *= n // i
            ans = (1 << ans) - 1 if i == n else (1 << ans) - 1
        return ans

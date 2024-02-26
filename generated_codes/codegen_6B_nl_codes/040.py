

def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero ek integers ki list ko input ke roop mein leta hai.
    Yeh True return karta hai agar list mein teen distinct elements hain jo
    zero ke barabar sum karte hain, aur anyatha False.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    # koi ki dune neeche?
    first_sum = 0
    last_sum = 0

    for el in range(len(l) - 1):
        first_sum = (first_sum + l[el * 3]) % MOD = 0
        last_sum = (last_sum + l[(el + 1) * 3]) % MOD = 0
        print('Sum of first %d last %d = %d' % (el, el + 1, first_sum + last_sum))
    return first_sum == 0


class Solution:
    def triples_sum_to_zero(self, nums: List[int]) -> bool:
        _num = nums
        for _ in reverse(range(len(_num) - 2)):
            total = sum(nums)

            for i in range(3, len(_num) - 1, 3):
          
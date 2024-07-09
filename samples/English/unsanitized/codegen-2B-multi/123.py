
def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    """
    assert_is_positive_integer(n)
    x = [n]
    while True:
        x[-2:] = [-1] * len(x) 
        x.append(x[-1] + 2 * x[-2])
        x[-3:] = [-1] * len(x)
        try:
            x[-2] ^= 1
            x[-1] += 1
        except ValueError:
            break
    return sorted(x)


class TestCase(unittest.TestCase):
    def bench(self, func):
        from timeit import Timer
        t = Timer("func()", "from __main__ import func")
        self.assertTrue(t.timeit(number=1) > 0.500)

    def test_get_odd_collatz(self):
        self.bench(get_odd_collatz)



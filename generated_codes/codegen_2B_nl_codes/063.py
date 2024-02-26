

def fibfib(n: int):
    """
    FibFib number sequence ek sequence hai jo Fibbonacci sequence ke saman hai aur iska definition is prakar hai:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Kripya ek function likhe jo efficiently fibfib number sequence ka n-th element compute kare.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n == 2:
        return 1
    # A FibFib algorithm (see: Wikipedia article) for calculating the sum of all natural numbers starting at
    # n-1:
    #     1. Define the base case. Here, we want to know how to sum 1 and 0. Note that we'll never want to sum 0
    #        again because the sum of 0 when multiplied by 2 is still 0.
    #    2. For all natural numbers k, we want to define how to compute fib(k).
    #    3. Fib(n) = ∑₁₉ 1 ≤ ⁁ ≤ n
    #    4. Fib(n) = n + fib(n-₁) + fib(n-₂) +… + fib(n-k)
    #    For this particular function, the terms are cumulative, so if the k-index n is a negative number, the term is
    #    evaluated backwards

    if n <
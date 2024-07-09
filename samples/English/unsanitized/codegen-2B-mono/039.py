

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    if n <= 1:
        return n

    f = ((FibbonacciIterator.next(F) + FibbonacciIterator.next(F)) for F in FibbonacciIterator(n))
    while True:
        if is_fib(next(f)):
            return next(f)

"""
Let's play around with prime iterator

>>> prime_iter = FibbonacciIterator(3)
>>> iter = FibonacciIterator(3)

>>> count(iter, iter.index)
1

>>> count(iter, prime_iter.index)
2
"""

prime_iter = FibonacciIterator(3)
iter = FibonacciIterator(3)





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
    if n == 2:
        return 1
    else:
        for i in range(2,n):
            if pow(i, 2)+pow(i+1, 2)!= n:
                continue
                fib_tot = pow(i, 2)+pow(i+1, 2)
                if fib_tot % 4 == 0:
                    return fib_tot


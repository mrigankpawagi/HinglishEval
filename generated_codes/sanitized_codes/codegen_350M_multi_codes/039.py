def prime_fib(n: int):
    """
    prime_fib woh n-th number return karta hai jo ek Fibonacci number bhi hai aur prime number bhi.
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
    # kara.fib(k) = fib(k)/2
    if n <= 0:
        return k // 10
    elif n % 2 == 0:
        return prime_fib(n / 2) + prime_fib(n / 2)
    # else
    if n == 1:
        return prime_fib(1)
    else:
        q = prime_fib(n)
        return q * prime_fib(n / 2)
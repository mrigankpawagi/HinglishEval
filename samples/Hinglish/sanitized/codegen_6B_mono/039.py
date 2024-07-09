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
    f = [2, 3]
    for i in range(2, n):
        f.append(f[-1] + f[-2])
    p = []
    for num in f:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            p.append(num)
    return p[-1]
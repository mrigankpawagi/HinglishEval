

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
    """   if n != 0:
        return prime_fib(n - 1) + prime_fib(n - 2)
    if n < 2:
        return n + 1
    karti_count = [1] * n
    karti_count[1] = 2
    for i in range(2, n):
        karti_count[i] = karti_count[i - 1] + karti_count[i - 2]
    return karti_count[n - 1]

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

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fib(num):
        if num <= 0:
            return 0
        elif num == 1:
            return 1
        else:
            return fib(num - 1) + fib(num - 2)

    count = 0
    i = 0
    while count < n:
        if is_prime(fib(i)):
            count += 1
        i += 1
    return fib(i - 1)

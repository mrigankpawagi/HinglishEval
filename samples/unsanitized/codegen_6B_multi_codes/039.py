

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
    if n == 1: return 2
    if n == 2: return 3
    first = prime_fib(n - 1)
    second = prime_fib(n - 2)
    return first + second


if __name__ == "__main__":
    simple_timer("Running Test", prime_fib, 10)

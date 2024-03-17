

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
    # We are trying to calculate next prime in Fibonacci sequence. If we can get one that will be number of prime's
    # so n-th number of Fibonacci sequence will also be prime number.

    prime = 2

    for i in range(0, len(prime_fib)):
        if prime_fib[i] % prime!= 0:
            prime = prime * prime_fib[i] + 1

    if prime_fib[len(prime_fib)] == 1:
        return 1
    else:
        number = prime_fib[len(prime_fib)] + prime_fib[len(prime_fib) - 1]
        prime_fib.append(1)
        return number

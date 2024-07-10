

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
    fibs_prime = []
    # create copy of Fibonacci list up to 15
    for fib in range(1,15):
        fibs_prime.insert(len(fibs_prime), prime_fib(fib))
    # iterate through all list
    for prime in range(15):
        # check if number is prime (it should be) and in list of Fibonacci primes
        if fibs_prime[prime] % 2 == 0 and (fibs_prime[prime] not in prime_fib(0) or prime_fib(0) in prime_fib(1)):
            fibs_prime.pop(prime)

    return max(fibs_prime)

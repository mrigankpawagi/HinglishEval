

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
    fibs = [2,3]
    primes = []
    for i in range(1,n):
        current_fib = fibs.pop()
        previous_fib = fibs.pop()
        next_fib = previous_fib + previous_fib
        while(next_fib < current_fib):
            fibs.append(next_fib)
            if(next_fib >= current_fib):
                primes.append(next_fib)
            next_fib += next_fib
    primes.append(current_fib) #The last number is prime.
    return primes


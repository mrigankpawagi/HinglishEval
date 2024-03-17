

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
    i = 1
    while i < n:
        z = num % i
        if z == 0:
            break
        z = num % i + 1
    if i==0:
        i = 0
    else:
        i = i**2
    if i>=n:
        return z, z**i
    z = pow(z,n)
    if z == n:
        return z, z**i
    return z, z**(n-i)

# ***********************
#       Fibonacci sequence test
#  **********************
    for j in range(0, n):
        print(prime_fib(j-1))
        print('    '*j) # i.e. Fibonacci number
        if prime_fib(j-1)%n == 1:
            print('         '*j)  # p(j, n) = pi(h, i)
            if prime_fib(j-1)*n == 1:
           
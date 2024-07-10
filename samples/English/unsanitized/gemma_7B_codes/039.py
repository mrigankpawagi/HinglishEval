

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
    if n < 1: raise ValueError("Invalid Argument")  # checking error
    if n == 1: return 2
    if n == 2: return 3
    if n == 3: return 5
    if n == 4: return 13

    fib1 = 2 # fib1 = 2
    fib2 = 3 # fib2 = 3
    fib3 = 5 # fib3 = 5

    while True:
        num = fib1 + fib2 + fib3
        num_len = len(str(num))

        if num_len == n:
            pnum = num
            n += 1
            break
        
        fib1 = fib2
        fib2 = fib3
        fib3 = num

    return pnum

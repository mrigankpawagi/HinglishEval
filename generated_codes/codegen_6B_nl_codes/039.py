

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
    a,b = 0,1
    while a<20 and (a==1 or b%a):
        a,b = b,a+b  
    if a==1 or a>20:
        return b
    else:
        return prime_fib(n-1)+prime_fib(n-2)

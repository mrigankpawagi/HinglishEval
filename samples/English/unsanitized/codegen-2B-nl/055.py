

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    a,b = b,a+b
    return a if n==1 else b if n==2 else fib(n-1) + fib(n-2)

print(fib(5))


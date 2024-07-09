

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    prev, curr = 0, 1
    for i in range(n):
        print(i, prev, curr)
        prev, curr = curr, prev + curr
    return curr
        

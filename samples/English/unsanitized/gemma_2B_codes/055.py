

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n==2 or n==1: return 1
    return fib(n-2) + fib(n-1)

def recur_fib(n: int):
    def helper(m: int, v: int):
        return m**2, m+v
    return fib(n)

if __name__=="__main__":
    import doctest
    doctest.testmod()

    print('>>> fib(1) == 1 : ', fib(1) == 1)
    print('>>> fib(2) == 1 : ', fib(2) == 1)
    print('>>> fib(3) == 2 : ', fib(3) == 2)

    print('\n')
    print('>>> recur_fib(1) == 1 : ', recur_fib(1) == 1)
    print('>>> recur_fib(2) == 1 : ', recur_fib(2) == 1)
    print('>>> recur_fib(3) == 2 : ', recur_fib(3) == 2)

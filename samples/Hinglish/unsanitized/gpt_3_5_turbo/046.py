def fib4(n: int):
    """
    Returns the n-th element of the fib4 number sequence.
    """
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        fib = [0, 0, 2]
        for i in range(3, n+1):
            fib.append(fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4])
        return fib[n]
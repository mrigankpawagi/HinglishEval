

def fib4(n: int):
    """
    Fib4 number sequence ek sequence hai jo Fibbonacci sequence ke saman hai, jo is prakar se define kiya gaya hai:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Kripya ek function likhe jo efficiently fib4 number sequence ka n-th element compute kare. Recursion ka use na kare.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    n = int(n)
    n -= 1
    n_prime = math.factorial(2 * n) - math.factorial(2 * n + 1)
    k = 0
    while n > 1:
        k *= n_prime
        k *= k
        n -= 1
    k += n
    return k


print('Eki Fibonacci sequence 1.', fib1())
print('Eki Fibonacci sequence 2.', fib2())

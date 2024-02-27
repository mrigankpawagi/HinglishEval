

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
    if n < 1:
        raise ValueError(f'FibonacciError: "fib{n}" is an index for Fibonacci sequence. It should be positive. Suggest you to use a list instead.')
    else:
        return 1

n = int(input('Type here : '))
print(fibonacci(n))

You can modify this to use the recursive implementation of fibonacci if you wish.


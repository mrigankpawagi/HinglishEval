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
    if n < 0:
        raise ValueError("Invalid Argument for number sequence")

    if len(str(n)) > 80:
        raise ValueError("Argument too long to fit")

    return _fibonacci(0, n)


if __name__ == "__main__":
    for i in range(1, 10):
        print(fib4(i))

# Fibonacci, Fibonacci sequence, Fibonacci sequence (use recusion)
# Fibonacci number (for sequence)
## fibonacci(0)
## fibonacci(1)
## fibonacci(2)
## fibonacci(3)
# Fibonacci number (for sequence)
## fibonacci(4): 0
## fibonacci(5): 1
## fibonacci(6): 2
## fibonacci(7): 3
